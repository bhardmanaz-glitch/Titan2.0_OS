"""
Titan2.0_OS

ODrive Axis

Titan actuator abstraction.

The axis coordinates motion and telemetry for a single
Titan joint while delegating all hardware communication
to a ControllerDriver implementation.

The axis contains no transport-specific or vendor-specific
logic.
"""


import time

from titan.hardware.axis_driver import AxisDriver
from titan.hardware.controller_driver import ControllerDriver
from titan.hardware.telemetry import Telemetry


class ODriveAxis(AxisDriver):

    def __init__(
        self,
        controller: ControllerDriver,
        channel: int,
    ):

        self._controller = controller
        self._channel = channel
        self._telemetry = None

    # ----------------------------------------------------

    def connect(self) -> None:

        self._controller.connect()

        self.refresh()

    # ----------------------------------------------------

    def enter_closed_loop(self) -> None:
        """
        Place the axis into CLOSED_LOOP_CONTROL.
        """

        if not self.connected:
            raise RuntimeError(
                "Axis is not connected."
            )

        self._controller.enter_closed_loop()

#-----------------------------------------------------------

    def enter_idle(self) -> None:
        """
        Return the axis to IDLE.
        """

        if not self.connected:
            raise RuntimeError(
                "ODriveAxis is not connected."
            )

        self._controller.enter_idle()


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

        self._controller.move_to(position)

    def wait_until_position(
        self,
        target: float,
        tolerance: float = 0.002,
        timeout: float = 3.0,
    ) -> None:
        """
        Wait until the axis reaches the requested position.
        """

        if not self.connected:
            raise RuntimeError(
                "ODriveAxis is not connected."
            )

        deadline = time.time() + timeout

        while time.time() < deadline:

            self.refresh()

            error = abs(self.position - target)

            print(
                f"Target={target:.5f} "
                f"Current={self.position:.5f} "
                f"Error={error:.5f}"
            )

            if error <= tolerance:
                return

            time.sleep(0.02)

        raise TimeoutError(
            f"Axis failed to reach {target:.5f} rev "
            f"(current={self.position:.5f})"
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
    
    def stop(self):

        self._controller.stop()

    #-----------------------------------------------------

    def disconnect(self):

        self._controller.disconnect()


    # ----------------------------------------------------

    def refresh(self) -> Telemetry:

        self._telemetry = self._controller.refresh()

        return self._telemetry
    # ----------------------------------------------------
    # Properties
    # ----------------------------------------------------

    @property
    def connected(self):
        return self._controller.connected

    @property
    def position(self):
        return self._telemetry.position

    @property
    def velocity(self):
        return self._telemetry.velocity

    @property
    def current(self):
        return self._telemetry.current

    @property
    def bus_voltage(self):
        return self._telemetry.bus_voltage

    @property
    def bus_current(self):
        return self._telemetry.bus_current

    @property
    def temperature(self):
        return self._telemetry.temperature

    @property
    def axis_state(self):
        return self._telemetry.axis_state

    @property
    def active_errors(self):
        return self._telemetry.active_errors

    @property
    def disarm_reason(self):
        return self._telemetry.disarm_reason
    
    @property
    def serial_number(self):
        return self._telemetry.serial_number

    @property
    def firmware_version(self):
        return self._telemetry.firmware_version# TEST FROM NANO
