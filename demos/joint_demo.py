from titan.hardware.odrive import ODriveAxis
from titan.hardware.joint import Joint

hip_motor = ODriveAxis(
    name="Left Hip Motor",
    axis_id=0,
)

hip = Joint(
    name="Left Hip",
    actuator=hip_motor,
    gear_ratio=36.0,
    min_angle=-1.4,
    max_angle=0.8,
)

hip.enable()

print("\nMove inside limits")
hip.move_safe(0.5)

print(f"Joint Angle : {hip.angle:.3f} rad")
print(f"Motor Turns : {hip.motor_position:.3f}")

print("\nRequest outside limits")
hip.move_safe(2.0)

print(f"Joint Angle : {hip.angle:.3f} rad")
print(f"Motor Turns : {hip.motor_position:.3f}")

hip.disable()