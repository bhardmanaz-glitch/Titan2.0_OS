import pytest

from titan.motion.foot_pose import FootPose
from titan.motion.leg_planner import LegPlanner
from titan.motion.trajectory import LegTrajectory


class FakeFootPlanner:

    def __init__(self):
        self.calls = []
        self.result = object()

    def generate(
        self,
        start,
        end,
        duration,
        dt,
    ):
        self.calls.append(
            (
                start,
                end,
                duration,
                dt,
            )
        )

        return self.result


class FakeTrajectoryMapper:

    def __init__(self):
        self.calls = []
        self.result = LegTrajectory(
            hip=object(),
            knee=object(),
        )

    def map(
        self,
        trajectory,
    ):
        self.calls.append(trajectory)
        return self.result


@pytest.fixture
def foot_planner():
    return FakeFootPlanner()


@pytest.fixture
def mapper():
    return FakeTrajectoryMapper()


@pytest.fixture
def planner(
    foot_planner,
    mapper,
):
    return LegPlanner(
        foot_planner=foot_planner,
        mapper=mapper,
    )


def test_create_leg_planner(
    foot_planner,
    mapper,
):

    planner = LegPlanner(
        foot_planner,
        mapper,
    )

    assert isinstance(
        planner,
        LegPlanner,
    )


def test_generate_delegates_to_foot_planner(
    planner,
    foot_planner,
):

    start = FootPose(
        0.30,
        -0.45,
    )

    end = FootPose(
        0.35,
        -0.45,
    )

    planner.generate(
        start,
        end,
        duration=1.0,
        dt=0.02,
    )

    assert foot_planner.calls == [
        (
            start,
            end,
            1.0,
            0.02,
        )
    ]


def test_generate_passes_trajectory_to_mapper(
    planner,
    foot_planner,
    mapper,
):

    planner.generate(
        FootPose(
            0.30,
            -0.45,
        ),
        FootPose(
            0.35,
            -0.45,
        ),
        duration=1.0,
        dt=0.02,
    )

    assert mapper.calls == [
        foot_planner.result,
    ]


def test_generate_returns_mapper_result(
    planner,
    mapper,
):

    result = planner.generate(
        FootPose(
            0.30,
            -0.45,
        ),
        FootPose(
            0.35,
            -0.45,
        ),
        duration=1.0,
        dt=0.02,
    )

    assert result is mapper.result