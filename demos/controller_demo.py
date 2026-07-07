from titan.hardware.odrive import ODriveAxis
from titan.hardware.joint import Joint

from titan.motion.planner import TrajectoryPlanner
from titan.control.joint_controller import JointController

motor = ODriveAxis(
    name="Hip",
    axis_id=0
)

joint = Joint(
    name="Hip",
    actuator=motor,
    gear_ratio=36,
    min_angle=-1.4,
    max_angle=0.8,
)

planner = TrajectoryPlanner()

trajectory = planner.generate(
    start=0,
    end=0.5
)

controller = JointController(joint)

controller.follow(trajectory)