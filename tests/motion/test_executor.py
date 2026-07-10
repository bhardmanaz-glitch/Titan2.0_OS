import time
import pytest

from titan.motion.trajectory import (
    MotionPoint,
    Trajectory,
)
from titan.motion.executor import TrajectoryExecutor
from titan.hardware.mock_axis import MockAxis


def test_create_executor():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    assert executor.driver is driver

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

def test_execute_returns_trajectory():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    result = executor.execute(trajectory)

    assert result is trajectory

def test_execute_visits_every_point():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    visited = []

    def record(point):
        visited.append(point)

    executor.process_point = record

    executor.execute(trajectory)

    assert len(visited) == len(trajectory)

def test_execute_commands_every_point():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    executor.execute(trajectory)

    assert driver.commanded_positions == [
        point.position
        for point in trajectory
    ]

def test_execute_moves_axis_to_final_position():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    executor.execute(trajectory)

    assert driver.position == trajectory.last.position

def test_wait_until_next_point():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    executor._wait_until_next_point(
        start_time=time.perf_counter(),
        dt=0.0,
    )

def test_executor_starts_not_running():

    executor = TrajectoryExecutor(MockAxis())

    assert executor.running is False

def test_executor_stop_requests_stop():

    executor = TrajectoryExecutor(MockAxis())

    executor.stop()

    assert executor.stop_requested

def test_execute_clears_stop_request():

    executor = TrajectoryExecutor(MockAxis())

    executor.stop()

    trajectory = create_trajectory()

    executor.execute(trajectory)

    assert executor.stop_requested is False

def test_execute_not_running_when_finished():

    executor = TrajectoryExecutor(MockAxis())

    trajectory = create_trajectory()

    executor.execute(trajectory)

    assert executor.running is False

def test_execute_calls_callback_for_every_point():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    visited = []

    executor.execute(
        trajectory,
        on_motion_point=visited.append,
    )

    assert len(visited) == len(trajectory)

def test_callback_receives_points_in_order():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    visited = []

    executor.execute(
        trajectory,
        on_motion_point=visited.append,
    )

    assert visited == trajectory.points

def test_execute_without_callback():

    driver = MockAxis()

    executor = TrajectoryExecutor(driver)

    trajectory = create_trajectory()

    executor.execute(trajectory)

def test_process_point_moves_axis():

    axis = MockAxis()

    executor = TrajectoryExecutor(axis)

    point = MotionPoint(
        position=3.5,
        velocity=0.0,
        acceleration=0.0,
        time=0.0,
        dt=0.02,
    )

    executor.process_point(point)

    assert axis.position == 3.5