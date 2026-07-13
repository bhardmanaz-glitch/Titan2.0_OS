"""
Titan2_OS

ODrive Axis Driver

Read-only interface to one calibrated ODrive axis.

Sprint 2:
    • Connect
    • Refresh telemetry
    • Read properties

No motion commands.
"""

from dataclasses import dataclass
import time

from titan.hardware.axis_driver import AxisDriver
from titan.hardware.telemetry import Telemetry

AXIS_STATE_IDLE = 1
AXIS_STATE_CLOSED_LOOP = 8

class ODriveAxis(AxisDriver):

    def __init__(
        self,
        serial_number: str | None = None,
        axis_index: int = 0,
    ):

        self._serial_number = serial_number
        self.axis_index = axis_index

        self._driver = None
        self._axis = None

        self._connected = False

        self._position = 0.0
        self._velocity = 0.0
        self._current = 0.0

        self._bus_voltage = 0.0
        self._bus_current = 0.0

        self._temperature = 0.0

        self._axis_state = "UNKNOWN"

        self._active_errors = []

        self._disarm_reason = None

        self._firmware_version = "Unknown"

        self._telemetry = None

    # ----------------------------------------------------

    def connect(self):

        try:
            import odrive
        except ImportError:
            raise RuntimeError(
                "The ODrive Python package is not installed."
            )

        self._driver = odrive.find_any(
            serial_number=self.serial_number
        )

        self._axis = (
            self._driver.axis0
            if self.axis_index == 0
            else self._driver.axis1
        )

        self._connected = True

        self.refresh()

    # ----------------------------------------------------

    def enter_closed_loop(self) -> None:
        """
        Place the axis into CLOSED_LOOP_CONTROL.
        """

        if not self.connected:
            raise RuntimeError(
                "ODriveAxis is not connected."
            )

        self._axis.requested_state = AXIS_STATE_CLOSED_LOOP

        time.sleep(0.1)

        if self._axis.current_state != AXIS_STATE_CLOSED_LOOP:
            raise RuntimeError(
                f"Failed to enter closed loop. Current state: {self._axis.current_state}"
            )

#-----------------------------------------------------------

    def enter_idle(self) -> None:
        """
        Return the axis to IDLE.
        """

        if not self.connected:
            raise RuntimeError(
                "ODriveAxis is not connected."
            )

        self._axis.requested_state = AXIS_STATE_CLOSED_LOOP

        time.sleep(0.1)

        if self._axis.current_state != AXIS_STATE_CLOSED_LOOP:
            raise RuntimeError(
                f"Failed to enter closed loop. Current state: {self._axis.current_state}"
            )

    #------------------------------------------------------

    def move_to(
        self,
        position: float,
    ) -> None:
        """
        Command the axis to a position.
        """

        if not self.connected:
            raise RuntimeError(
                "ODriveAxis is not connected."
            )

        self._axis.controller.input_pos = position
    
    def set_velocity(
        self,
        velocity: float,
    ) -> None:
        """
        Command the axis to a velocity.

        Hardware implementation coming in a future commit.
        """

        raise NotImplementedError(
            "ODrive velocity control not implemented yet."
        )
    
    def stop(self) -> None:
        """
        Stop the axis safely.

        Hardware implementation coming in a future commit.
        """

        raise NotImplementedError(
            "ODrive stop not implemented yet."
        )

    #-----------------------------------------------------

    def disconnect(self):

        self._driver = None

        self._axis = None

        self._connected = False

    # ----------------------------------------------------

    def refresh(self) -> Telemetry:

        if not self.connected:
            raise RuntimeError(
                "ODriveAxis is not connected."
            )

        #
        # Read hardware
        #
        self._position = self._axis.pos_estimate
        self._velocity = self._axis.vel_estimate

        self._current = self._axis.motor.foc.Iq_measured

        self._bus_voltage = self._driver.vbus_voltage
        self._bus_current = self._driver.ibus

        self._temperature = self._driver.thermistor0

        self._axis_state = str(self._axis.current_state)

        self._active_errors = self._axis.active_errors
        self._disarm_reason = self._axis.disarm_reason

        self._firmware_version = (
            f"{self._driver.fw_version_major}."
            f"{self._driver.fw_version_minor}."
            f"{self._driver.fw_version_revision}"
        )

        #
        # Snapshot
        #
        self._telemetry = Telemetry(
            position=self._position,
            velocity=self._velocity,
            current=self._current,
            temperature=self._temperature,
            bus_voltage=self._bus_voltage,
            bus_current=self._bus_current,
            axis_state=self._axis_state,
            active_errors=tuple(self._active_errors or ()),
            disarm_reason=self._disarm_reason,
        )

        return self._telemetry
    # ----------------------------------------------------
    # Properties
    # ----------------------------------------------------

    @property
    def connected(self):
        return self._connected

    @property
    def position(self):
        return self._telemetry.position

    @property
    def velocity(self):
        return self._velocity

    @property
    def current(self):
        return self._current

    @property
    def bus_voltage(self):
        return self._bus_voltage

    @property
    def bus_current(self):
        return self._bus_current

    @property
    def temperature(self):
        return self._temperature

    @property
    def axis_state(self):
        return self._axis_state

    @property
    def active_errors(self):
        return self._active_errors

    @property
    def disarm_reason(self):
        return self._disarm_reason
    
    @property
    def serial_number(self):
        return self._serial_number

    @property
    def firmware_version(self):
        return self._firmware_version