from titan.hardware.odrive import ODriveAxis

hip = ODriveAxis(
    name="Hip",
    axis_id=0
)

hip.enable()

hip.set_position(1.5)

hip.heartbeat()

hip.disable()