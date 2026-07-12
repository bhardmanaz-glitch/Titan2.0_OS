import pytest

from titan.motion.robot_executor import RobotExecutor


@pytest.fixture
def robot_executor(
    left_front_leg_executor,
    right_front_leg_executor,
    left_rear_leg_executor,
    right_rear_leg_executor,
):
    return RobotExecutor(
        left_front=left_front_leg_executor,
        right_front=right_front_leg_executor,
        left_rear=left_rear_leg_executor,
        right_rear=right_rear_leg_executor,
    )