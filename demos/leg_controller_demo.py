from titan.hardware.odrive import ODriveAxis
from titan.hardware.joint import Joint

from titan.motion.planner import TrajectoryPlanner
from titan.motion.trajectory import LegTrajectory

from titan.control.leg_controller import LegController


# -----------------------
# Motors
# -----------------------

hip_motor = ODriveAxis(
    name="Hip",
    axis_id=0,
)

knee_motor = ODriveAxis(
    name="Knee",
    axis_id=1,
)


# -----------------------
# Joints
# -----------------------

hip_joint = Joint(
    name="Hip",
    actuator=hip_motor,
    gear_ratio=36,
    min_angle=-1.4,
    max_angle=0.8,
)

knee_joint = Joint(
    name="Knee",
    actuator=knee_motor,
    gear_ratio=36,
    min_angle=-2.4,
    max_angle=0.0,
)


# -----------------------
# Planner
# -----------------------

planner = TrajectoryPlanner()

hip_path = planner.generate(
    start=0.0,
    end=0.5,
)

knee_path = planner.generate(
    start=-0.5,
    end=0.0,
)


# -----------------------
# Leg Trajectory
# -----------------------

trajectory = LegTrajectory(
    hip=hip_path,
    knee=knee_path,
)


# -----------------------
# Controller
# -----------------------

controller = LegController(
    hip_joint,
    knee_joint,
)

controller.follow(trajectory)