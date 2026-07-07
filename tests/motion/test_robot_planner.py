import pytest

from titan.motion.robot_trajectory import RobotTrajectory
from titan.motion.trajectory import LegTrajectory


def test_generate_returns_robot_trajectory(robot_planner):

    trajectory = robot_planner.generate(
        front_left_start=(.100, -.1500),
        front_left_end=(.120, -.1500),

        front_right_start=(.100, -.1500),
        front_right_end=(.120, -.1500),

        rear_left_start=(.100, -.1500),
        rear_left_end=(.120, -.1500),

        rear_right_start=(.100, -.1500),
        rear_right_end=(.120, -.1500),

        dt=0.02,
    )

    assert isinstance(trajectory, RobotTrajectory)


def test_contains_four_leg_trajectories(robot_planner):

    trajectory = robot_planner.generate(
        front_left_start=(.100, -.1500),
        front_left_end=(.120, -.1500),

        front_right_start=(.100, -.1500),
        front_right_end=(.120, -.1500),

        rear_left_start=(.100, -.1500),
        rear_left_end=(.120, -.1500),

        rear_right_start=(.100, -.1500),
        rear_right_end=(.120, -.1500),
    )

    assert isinstance(trajectory.front_left, LegTrajectory)
    assert isinstance(trajectory.front_right, LegTrajectory)
    assert isinstance(trajectory.rear_left, LegTrajectory)
    assert isinstance(trajectory.rear_right, LegTrajectory)


def test_all_leg_durations_match(robot_planner):

    trajectory = robot_planner.generate(
        front_left_start=(.100, -.1500),
        front_left_end=(.120, -.1500),

        front_right_start=(.100, -.1500),
        front_right_end=(.120, -.1500),

        rear_left_start=(.100, -.1500),
        rear_left_end=(.120, -.1500),

        rear_right_start=(.100, -.1500),
        rear_right_end=(.120, -.1500),
    )

    durations = [
        trajectory.front_left.duration,
        trajectory.front_right.duration,
        trajectory.rear_left.duration,
        trajectory.rear_right.duration,
    ]

    assert len(set(durations)) == 1