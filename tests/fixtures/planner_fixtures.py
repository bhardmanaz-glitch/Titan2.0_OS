import pytest

from titan.motion.planner import TrajectoryPlanner
from titan.motion.profiles import (
    LinearProfile,
    TrapezoidalProfile,
)


@pytest.fixture
def linear_planner():

    return TrajectoryPlanner(
        profile=LinearProfile(),
    )


@pytest.fixture
def trapezoidal_planner():

    return TrajectoryPlanner(
        profile=TrapezoidalProfile(),
    )