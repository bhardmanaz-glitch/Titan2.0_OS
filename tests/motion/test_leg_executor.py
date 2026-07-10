from titan.motion.trajectory import (
    MotionPoint,
    Trajectory,
    LegTrajectory,
)

from titan.hardware.mock_axis import MockAxis
from titan.motion.executor import TrajectoryExecutor
from titan.motion.leg_executor import LegExecutor


def test_create_leg_executor():

    hip = TrajectoryExecutor(MockAxis())
    knee = TrajectoryExecutor(MockAxis())

    executor = LegExecutor(
        hip_executor=hip,
        knee_executor=knee,
    )

    assert executor.hip_executor is hip
    assert executor.knee_executor is knee

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

def test_execute_returns_leg_trajectory():

    leg = create_leg_trajectory()

    hip = TrajectoryExecutor(MockAxis())
    knee = TrajectoryExecutor(MockAxis())

    executor = LegExecutor(
        hip_executor=hip,
        knee_executor=knee,
    )

    result = executor.execute(leg)

    assert result is leg

def test_execute_moves_both_axes():

    hip_axis = MockAxis()
    knee_axis = MockAxis()

    executor = LegExecutor(
        hip_executor=TrajectoryExecutor(hip_axis),
        knee_executor=TrajectoryExecutor(knee_axis),
    )

    leg = create_leg_trajectory()

    executor.execute(leg)

    assert hip_axis.position == leg.hip.last.position
    assert knee_axis.position == leg.knee.last.position

def test_execute_different_length_trajectories():

    hip_axis = MockAxis()
    knee_axis = MockAxis()

    executor = LegExecutor(
        hip_executor=TrajectoryExecutor(hip_axis),
        knee_executor=TrajectoryExecutor(knee_axis),
    )

    trajectory = LegTrajectory(
        hip=create_long_trajectory(),
        knee=create_short_trajectory(),
    )

    executor.execute(trajectory)

    assert hip_axis.position == 4.0
    assert knee_axis.position == 1.0