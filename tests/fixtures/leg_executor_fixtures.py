import pytest

from titan.motion.leg_executor import LegExecutor


@pytest.fixture
def left_front_leg_executor(
    left_front_hip_joint,
    left_front_knee_joint,
):
    return LegExecutor(
        hip_joint=left_front_hip_joint,
        knee_joint=left_front_knee_joint,
    )


@pytest.fixture
def right_front_leg_executor(
    right_front_hip_joint,
    right_front_knee_joint,
):
    return LegExecutor(
        hip_joint=right_front_hip_joint,
        knee_joint=right_front_knee_joint,
    )


@pytest.fixture
def left_rear_leg_executor(
    left_rear_hip_joint,
    left_rear_knee_joint,
):
    return LegExecutor(
        hip_joint=left_rear_hip_joint,
        knee_joint=left_rear_knee_joint,
    )


@pytest.fixture
def right_rear_leg_executor(
    right_rear_hip_joint,
    right_rear_knee_joint,
):
    return LegExecutor(
        hip_joint=right_rear_hip_joint,
        knee_joint=right_rear_knee_joint,
    )