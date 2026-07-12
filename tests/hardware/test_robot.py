from titan.hardware.robot import Robot
from titan.hardware.prototype import (
    PROTOTYPE_ROBOT,
    PROTOTYPE_LEG,
)


def test_robot_is_robot():

    assert isinstance(
        PROTOTYPE_ROBOT,
        Robot,
    )


def test_robot_contains_four_legs():

    assert PROTOTYPE_ROBOT.left_front is PROTOTYPE_LEG
    assert PROTOTYPE_ROBOT.right_front is PROTOTYPE_LEG
    assert PROTOTYPE_ROBOT.left_rear is PROTOTYPE_LEG
    assert PROTOTYPE_ROBOT.right_rear is PROTOTYPE_LEG