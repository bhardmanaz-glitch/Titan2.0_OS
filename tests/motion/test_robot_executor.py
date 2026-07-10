import pytest

from titan.motion.robot_executor import RobotExecutor
from titan.motion.robot_trajectory import RobotTrajectory
from titan.motion.trajectory import (
    LegTrajectory,
    MotionPoint,
    Trajectory,
)


class FakeLegExecutor:
    """Simple fake used to verify RobotExecutor behavior."""

    def __init__(self):
        self.executed = False
        self.trajectory = None

    def execute(self, trajectory):
        self.executed = True
        self.trajectory = trajectory
        return trajectory


def create_leg_trajectory() -> LegTrajectory:
    """Create a minimal one-point leg trajectory."""

    point = MotionPoint(
        position=0.0,
        velocity=0.0,
        acceleration=0.0,
        time=0.0,
        dt=0.02,
    )

    axis = Trajectory(
        points=[point],
        duration=0.0,
        distance=0.0,
        dt=0.02,
        start=0.0,
        end=0.0,
    )

    return LegTrajectory(
        hip=axis,
        knee=axis,
    )


def create_robot_trajectory() -> RobotTrajectory:
    """Create a minimal robot trajectory."""

    return RobotTrajectory(
        left_front=create_leg_trajectory(),
        right_front=create_leg_trajectory(),
        left_rear=create_leg_trajectory(),
        right_rear=create_leg_trajectory(),
    )


def test_create_robot_executor():

    executor = RobotExecutor(
        left_front=FakeLegExecutor(),
        right_front=FakeLegExecutor(),
        left_rear=FakeLegExecutor(),
        right_rear=FakeLegExecutor(),
    )

    assert isinstance(executor, RobotExecutor)


def test_executor_stores_leg_executors():

    lf = FakeLegExecutor()
    rf = FakeLegExecutor()
    lr = FakeLegExecutor()
    rr = FakeLegExecutor()

    executor = RobotExecutor(
        left_front=lf,
        right_front=rf,
        left_rear=lr,
        right_rear=rr,
    )

    assert executor.left_front is lf
    assert executor.right_front is rf
    assert executor.left_rear is lr
    assert executor.right_rear is rr


def test_execute_requires_robot_trajectory():

    executor = RobotExecutor(
        left_front=FakeLegExecutor(),
        right_front=FakeLegExecutor(),
        left_rear=FakeLegExecutor(),
        right_rear=FakeLegExecutor(),
    )

    with pytest.raises(TypeError):
        executor.execute(None)


def test_execute_runs_every_leg():

    lf = FakeLegExecutor()
    rf = FakeLegExecutor()
    lr = FakeLegExecutor()
    rr = FakeLegExecutor()

    executor = RobotExecutor(
        left_front=lf,
        right_front=rf,
        left_rear=lr,
        right_rear=rr,
    )

    robot = create_robot_trajectory()

    result = executor.execute(robot)

    assert result is robot

    assert lf.executed
    assert rf.executed
    assert lr.executed
    assert rr.executed

    assert lf.trajectory is robot.left_front
    assert rf.trajectory is robot.right_front
    assert lr.trajectory is robot.left_rear
    assert rr.trajectory is robot.right_rear