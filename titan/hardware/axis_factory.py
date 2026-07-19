from titan.hardware.odrive_axis import ODriveAxis


class AxisFactory:

    @staticmethod
    def create(
        hardware,
        controller,
    ):

        if hardware.controller_type == "odrive":

            return ODriveAxis(
                controller=controller,
                channel=hardware.controller_channel,
            )

        raise RuntimeError(
            f"Unknown controller type '{hardware.controller_type}'."
        )