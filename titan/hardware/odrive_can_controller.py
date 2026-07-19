import struct

import can

from titan.hardware.can_bus import CANBus
from titan.hardware.controller_driver import ControllerDriver
from titan.hardware.telemetry import Telemetry


#
# ODrive CAN Commands
#
SET_AXIS_STATE = 0x07
SET_INPUT_POS = 0x0C

#
# ODrive Axis States
#
AXIS_STATE_IDLE = 1
AXIS_STATE_CLOSED_LOOP = 8


class ODriveCANController(ControllerDriver):
    """
    ODrive Controller implementation using SocketCAN.

    This class translates Titan controller operations into
    ODrive CAN protocol messages.

    It owns no CAN socket. All communication flows through
    the shared CANBus instance.
    """

    def __init__(
        self,
        bus: CANBus,
        node_id: int,
    ):

        self._bus = bus

        self._node_id = node_id

        self._connected = False

        self._telemetry = None

    # -----------------------------------------------------

    def _arbitration_id(
        self,
        command: int,
    ) -> int:

        return (
            (self._node_id << 5)
            | command
        )

    # -----------------------------------------------------

    @property
    def connected(self):

        return self._connected

    # -----------------------------------------------------

    def connect(self) -> None:

        if not self._bus.connected:

            raise RuntimeError(
                "CAN bus is not connected."
            )

        self._connected = True

    # -----------------------------------------------------

    def disconnect(self) -> None:

        self._connected = False

    # -----------------------------------------------------

    def enter_closed_loop(self) -> None:

        if not self.connected:

            raise RuntimeError(
                "Controller not connected."
            )

        message = can.Message(

            arbitration_id=self._arbitration_id(
                SET_AXIS_STATE
            ),

            data=struct.pack(
                "<I",
                AXIS_STATE_CLOSED_LOOP,
            ),

            is_extended_id=False,

        )

        self._bus.send(message)

    # -----------------------------------------------------

    def enter_idle(self) -> None:

        if not self.connected:

            raise RuntimeError(
                "Controller not connected."
            )

        message = can.Message(

            arbitration_id=self._arbitration_id(
                SET_AXIS_STATE
            ),

            data=struct.pack(
                "<I",
                AXIS_STATE_IDLE,
            ),

            is_extended_id=False,

        )

        self._bus.send(message)

    # -----------------------------------------------------

    def move_to(
        self,
        position: float,
    ) -> None:

        if not self.connected:

            raise RuntimeError(
                "Controller not connected."
            )

        message = can.Message(

            arbitration_id=self._arbitration_id(
                SET_INPUT_POS
            ),

            data=struct.pack(
                "<fhh",
                position,
                0,
                0,
            ),

            is_extended_id=False,

        )

        self._bus.send(message)

    # -----------------------------------------------------

    def stop(self) -> None:

        self.enter_idle()

    # -----------------------------------------------------

    def set_velocity(
        self,
        velocity: float,
    ) -> None:

        raise NotImplementedError(
            "CAN velocity control not implemented yet."
        )

    # -----------------------------------------------------

    def refresh(self) -> Telemetry:

        raise NotImplementedError(
            "CAN telemetry will be implemented in the next commit."
        )