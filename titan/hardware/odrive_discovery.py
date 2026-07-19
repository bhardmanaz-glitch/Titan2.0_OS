from titan.hardware.controller_discovery import ControllerDiscovery

class ODriveDiscovery(ControllerDiscovery):

    def find(
        self,
        address: str,
    ):
        import odrive

        try:
            return odrive.find_sync(
                serial_number=str(address),
                timeout=5,
            )

        except TimeoutError:

            raise RuntimeError(
                f"Controller {address} not found."
            )

    def list_addresses(self):

        return [
            str(controller.serial_number)
            for controller in self.enumerate()
        ]