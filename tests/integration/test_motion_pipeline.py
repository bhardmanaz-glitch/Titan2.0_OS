import pytest

from titan.motion.trajectory import LegTrajectory
from titan.motion.foot_pose import FootPose

def test_motion_pipeline_returns_leg_trajectory(
    leg_planner,
):

    trajectory = leg_planner.generate(
        foot_start=FootPose(
            x=0.10,
            y=-0.15,
        ),
        foot_end=FootPose(
            x=0.15,
            y=-0.15,
        ),
        duration=1.0,
        dt=0.02,
    )

    assert isinstance(
        trajectory,
        LegTrajectory,
    )

def test_motion_pipeline_joint_counts_match(
    leg_planner,
):

    trajectory = leg_planner.generate(
        foot_start=FootPose(0.10, -0.15),
        foot_end=FootPose(0.15, -0.15),
        duration=1.0,
        dt=0.02,
    )

    assert len(trajectory.hip) == len(trajectory.knee)
    assert trajectory.hip.duration == pytest.approx(1.0)
    assert trajectory.knee.duration == pytest.approx(1.0)

    assert trajectory.hip.dt == pytest.approx(0.02)
    assert trajectory.knee.dt == pytest.approx(0.02)

    assert trajectory.hip.first.position != trajectory.hip.last.position
    assert trajectory.knee.first.position != trajectory.knee.last.position