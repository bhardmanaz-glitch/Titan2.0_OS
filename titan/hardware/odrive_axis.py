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

from titan.hardware.axis_driver import AxisDriver
from titan.hardware.telemetry import Telemetry


@dataclass
class ODriveAxis(AxisDriver):

    serial_number: str | None = None

    axis_index: int = 0

    _driver = None

    _axis = None

    _connected: bool = False

    _position: float = 0.0
    _velocity: float = 0.0
    _current: float = 0.0

    _bus_voltage: float = 0.0
    _bus_current: float = 0.0

    _temperature: float = 0.0

    _axis_state: str = "UNKNOWN"

    _active_errors: list = None

    _disarm_reason = None

    _firmware_version: str = "Unknown"

    # ----------------------------------------------------

    def connect(self):

        import odrive

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

    def move_to(
        self,
        position: float,
    ) -> None:
        """
        Command the axis to a position.

            Hardware implementation coming in a future commit.
        """

        raise NotImplementedError(
            "ODrive position control not implemented yet."
        )
    
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
    def firmware_version(self):
        return self._firmware_version