import pytest

from titan.hardware.prototype import PROTOTYPE_LEG

from titan.kinematics.inverse_kinematics import (
    InverseKinematics,
)

from titan.motion.behaviors import (
    TrapezoidalBehavior,
)

from titan.motion.foot_planner import (
    FootPlanner,
)

from titan.motion.trajectory_mapper import (
    TrajectoryMapper,
)

from titan.motion.leg_planner import (
    LegPlanner,
)


@pytest.fixture
def inverse_kinematics():

    return InverseKinematics(
        PROTOTYPE_LEG,
    )


@pytest.fixture
def trapezoidal_behavior():

    return TrapezoidalBehavior()


@pytest.fixture
def foot_planner(
    trapezoidal_behavior,
):

    return FootPlanner(
        behavior=trapezoidal_behavior,
    )


@pytest.fixture
def trajectory_mapper(
    inverse_kinematics,
):

    return TrajectoryMapper(
        inverse_kinematics,
    )


@pytest.fixture
def leg_planner(
    foot_planner,
    trajectory_mapper,
):

    return LegPlanner(
        foot_planner=foot_planner,
        mapper=trajectory_mapper,
    )