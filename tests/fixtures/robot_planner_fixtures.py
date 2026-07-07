import pytest

from titan.motion.robot_planner import RobotTrajectoryPlanner
from titan.motion.leg_planner import LegPlanner


@pytest.fixture
def robot_planner(
    ik_solver,
    linear_planner,
):
    leg = LegPlanner(
        ik_solver=ik_solver,
        trajectory_planner=linear_planner,
    )

    return RobotTrajectoryPlanner(
        front_left=leg,
        front_right=leg,
        rear_left=leg,
        rear_right=leg,
    )