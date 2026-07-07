import pytest

from titan.motion.leg_planner import LegPlanner


@pytest.fixture
def leg_planner(
    ik_solver,
    linear_planner,
):
    return LegPlanner(
        ik_solver=ik_solver,
        trajectory_planner=linear_planner,
    )