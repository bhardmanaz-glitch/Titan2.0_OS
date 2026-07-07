import pytest

from titan.motion.trajectory import (
    LegTrajectory,
    Trajectory,
)

def test_generate_returns_leg_trajectory(leg_planner):

    leg = leg_planner.generate(
        foot_start=(.100, -.150),
        foot_end=(.150, -.150),
    )

    assert isinstance(leg, LegTrajectory)

def test_hip_is_trajectory(leg_planner):

    leg = leg_planner.generate(
        foot_start=(.100, -.150),
        foot_end=(.150, -.150),
    )

    assert isinstance(leg.hip, Trajectory)

def test_knee_is_trajectory(leg_planner):

    leg = leg_planner.generate(
        foot_start=(.100, -.150),
        foot_end=(.150, -.150),
    )

    assert isinstance(leg.knee, Trajectory)

def test_joint_sample_counts_match(leg_planner):

    leg = leg_planner.generate(
        foot_start=(.100, -.150),
        foot_end=(.150, -.150),
    )

    assert len(leg.hip) == len(leg.knee)

def test_duration_matches(leg_planner):

    leg = leg_planner.generate(
        foot_start=(.100, -.150),
        foot_end=(.150, -.150),
    )

    assert leg.hip.duration == pytest.approx(
        leg.knee.duration
    )

def test_reverse_motion(leg_planner):

    leg = leg_planner.generate(
        foot_start=(.150, -.150),
        foot_end=(.100, -.150),
    )

    assert leg.hip[0].position > leg.hip[-1].position

