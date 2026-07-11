import pytest

from titan.kinematics.inverse_kinematics import InverseKinematics
from titan.motion.foot_pose import FootPose
from titan.motion.trajectory import LegTrajectory, MotionPoint, Trajectory
from titan.motion.trajectory_mapper import TrajectoryMapper
from titan.motion.joint_pose import JointPose


class FakeInverseKinematics:

    def solve(
        self,
        pose: FootPose,
    ) -> JointPose:

        return JointPose(
            hip=1.0,
            knee=2.0,
        )

@pytest.fixture
def mapper():

    return TrajectoryMapper(
        FakeInverseKinematics(),
    )


@pytest.fixture
def trajectory():

    return Trajectory(
        points=[
            MotionPoint(
                position=FootPose(0.30, -0.45),
                velocity=0.0,
                acceleration=0.0,
                time=0.0,
                dt=0.02,
            ),
            MotionPoint(
                position=FootPose(0.31, -0.44),
                velocity=0.0,
                acceleration=0.0,
                time=0.02,
                dt=0.02,
            ),
            MotionPoint(
                position=FootPose(0.32, -0.43),
                velocity=0.0,
                acceleration=0.0,
                time=0.04,
                dt=0.02,
            ),
        ],
        duration=0.04,
        distance=0.02,
        dt=0.02,
        start=FootPose(0.30, -0.45),
        end=FootPose(0.32, -0.43),
    )


def test_returns_leg_trajectory(
    mapper,
    trajectory,
):
    leg = mapper.map(trajectory)
    assert isinstance(leg, LegTrajectory)


def test_preserves_sample_count(
    mapper,
    trajectory,
):
    leg = mapper.map(trajectory)

    assert len(leg.hip) == len(trajectory)
    assert len(leg.knee) == len(trajectory)


def test_preserves_duration(
    mapper,
    trajectory,
):
    leg = mapper.map(trajectory)

    assert leg.duration == trajectory.duration


def test_preserves_dt(
    mapper,
    trajectory,
):
    leg = mapper.map(trajectory)

    assert leg.hip.dt == trajectory.dt
    assert leg.knee.dt == trajectory.dt


def test_maps_every_sample(
    mapper,
    trajectory,
):

    leg = mapper.map(trajectory)

    assert all(
        point.position == 1.0
        for point in leg.hip
    )

    assert all(
        point.position == 2.0
        for point in leg.knee
    )