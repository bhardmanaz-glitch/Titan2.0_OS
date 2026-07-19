from titan.hardware.can_bus import CANBus

from titan.hardware.odrive_can_controller import (
    ODriveCANController,
)

from titan.hardware.odrive_usb_controller import (
    ODriveUSBController,
)


class ControllerFactory:

    _can_bus = CANBus()

    @classmethod
    def create(
        cls,
        hardware,
    ):

        #
        # ODrive
        #

        if hardware.controller_type == "odrive":

            #
            # CAN
            #

            if hardware.transport == "can":

                if not cls._can_bus.connected:

                    cls._can_bus.connect()

                return ODriveCANController(

                    bus=cls._can_bus,

                    node_id=hardware.controller_address,

                )

            #
            # USB
            #

            if hardware.transport == "usb":

                return ODriveUSBController(

                    serial_number=hardware.controller_address,

                    channel=hardware.controller_channel,

                )

        raise RuntimeError(

            f"Unsupported controller "
            f"{hardware.controller_type} "
            f"over {hardware.transport}"

        )