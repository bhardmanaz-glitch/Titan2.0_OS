import pytest

from titan.motion import trajectory
from titan.motion.trajectory import (
    MotionPoint,
    Trajectory,
    LegTrajectory,
)
from titan.motion.leg_executor import LegExecutor


def test_create_leg_executor(
    leg_executor,
    hip_joint,
    knee_joint,
):

    assert leg_executor.hip_joint is hip_joint
    assert leg_executor.knee_joint is knee_joint

    assert leg_executor.hip_executor.joint is hip_joint
    assert leg_executor.knee_executor.joint is knee_joint

def create_trajectory():

    return Trajectory(
        points=[
            MotionPoint(
                position=0.0,
                velocity=0.0,
                acceleration=0.0,
                time=0.0,
                dt=0.02,
            ),
            MotionPoint(
                position=1.0,
                velocity=0.0,
                acceleration=0.0,
                time=0.02,
                dt=0.02,
            ),
        ],
        duration=0.02,
        distance=1.0,
        dt=0.02,
        start=0.0,
        end=1.0,
    )

def create_short_trajectory():

    return Trajectory(
        points=[
            MotionPoint(
                position=0.0,
                velocity=0.0,
                acceleration=0.0,
                time=0.0,
                dt=0.02,
            ),
            MotionPoint(
                position=1.0,
                velocity=0.0,
                acceleration=0.0,
                time=0.02,
                dt=0.02,
            ),
        ],
        duration=0.02,
        distance=1.0,
        dt=0.02,
        start=0.0,
        end=1.0,
    )

def create_long_trajectory():

    return Trajectory(
        points=[
            MotionPoint(0.0,0.0,0.0,0.00,0.02),
            MotionPoint(1.0,0.0,0.0,0.02,0.02),
            MotionPoint(2.0,0.0,0.0,0.04,0.02),
            MotionPoint(3.0,0.0,0.0,0.06,0.02),
            MotionPoint(4.0,0.0,0.0,0.08,0.02),
        ],
        duration=0.08,
        distance=4.0,
        dt=0.02,
        start=0.0,
        end=4.0,
    )


def create_leg_trajectory():

    return LegTrajectory(
        hip=create_trajectory(),
        knee=create_trajectory(),
    )

def test_execute_returns_leg_trajectory(
    leg_executor,
):

    leg = create_leg_trajectory()

    result = leg_executor.execute(leg)

    assert result is leg

def test_execute_moves_both_axes(
    leg_executor,
    hip_joint,
    knee_joint,
):

    leg = create_leg_trajectory()

    leg_executor.execute(leg)

    expected_hip = hip_joint.mapper.map(
        leg.hip.last.position
    )

    expected_knee = knee_joint.mapper.map(
        leg.knee.last.position
    )

    assert hip_joint.driver.position == pytest.approx(
        expected_hip.position
    )

    assert knee_joint.driver.position == pytest.approx(
        expected_knee.position
)   

def test_execute_different_length_trajectories(
    leg_executor,
    hip_joint,
    knee_joint,
):

    trajectory = LegTrajectory(
        hip=create_long_trajectory(),
        knee=create_short_trajectory(),
    )

    leg_executor.execute(trajectory)

    expected_hip = hip_joint.mapper.map(4.0)

    assert hip_joint.driver.position == pytest.approx(
        expected_hip.position
    )

    expected_knee = knee_joint.mapper.map(1.0)

    assert knee_joint.driver.position == pytest.approx(
        expected_knee.position
    )