import pytest

from titan.motion.robot_trajectory import RobotTrajectory
from titan.motion.trajectory import LegTrajectory


def test_generate_returns_robot_trajectory(robot_planner):

    trajectory = robot_planner.generate(
        left_front_start=(.100, -.150),
        left_front_end=(.120, -.150),

        right_front_start=(.100, -.150),
        right_front_end=(.120, -.150),

        left_rear_start=(.100, -.150),
        left_rear_end=(.120, -.150),

        right_rear_start=(.100, -.150),
        right_rear_end=(.120, -.150),

        dt=0.02,
    )

    assert isinstance(trajectory, RobotTrajectory)


def test_contains_four_leg_trajectories(robot_planner):

    trajectory = robot_planner.generate(
        left_front_start=(.100, -.150),
        left_front_end=(.120, -.150),

        right_front_start=(.100, -.150),
        right_front_end=(.120, -.150),

        left_rear_start=(.100, -.150),
        left_rear_end=(.120, -.150),

        right_rear_start=(.100, -.150),
        right_rear_end=(.120, -.150),
    )

    assert isinstance(trajectory.left_front, LegTrajectory)
    assert isinstance(trajectory.right_front, LegTrajectory)
    assert isinstance(trajectory.left_rear, LegTrajectory)
    assert isinstance(trajectory.right_rear, LegTrajectory)


def test_all_leg_durations_match(robot_planner):

    trajectory = robot_planner.generate(
        left_front_start=(.100, -.150),
        left_front_end=(.120, -.150),

        right_front_start=(.100, -.150),
        right_front_end=(.120, -.150),

        left_rear_start=(.100, -.150),
        left_rear_end=(.120, -.150),

        right_rear_start=(.100, -.150),
        right_rear_end=(.120, -.150),
    )

    durations = [
        trajectory.left_front.duration,
        trajectory.right_front.duration,
        trajectory.left_rear.duration,
        trajectory.right_rear.duration,
    ]

    assert len(set(durations)) == 1