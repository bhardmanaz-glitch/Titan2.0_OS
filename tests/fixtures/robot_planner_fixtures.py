import pytest

from titan.motion.robot_planner import RobotTrajectoryPlanner
from titan.motion.leg_planner import LegPlanner


@pytest.fixture
def robot_planner(
    leg_planner,
):

    return RobotTrajectoryPlanner(
        left_front=leg_planner,
        right_front=leg_planner,
        left_rear=leg_planner,
        right_rear=leg_planner,
    )