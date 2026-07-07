import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.motor import Motor
from titan.hardware.gearbox import Gearbox
from titan.hardware.actuator import Actuator
from titan.hardware.joint import Joint


def create_joint():

    motor = Motor(name="GL40")

    gearbox = Gearbox(
        name="Planetary",
        ratio=36.0,
    )

    actuator = Actuator(
        motor=motor,
        gearbox=gearbox,
    )

    return Joint(
        name="Hip",
        actuator=actuator,
        min_angle=-1.5,
        max_angle=1.5,
    )


def test_create_joint():

    joint = create_joint()

    assert joint.name == "Hip"


def test_joint_limits():

    joint = create_joint()

    assert joint.min_angle == -1.5
    assert joint.max_angle == 1.5


def test_joint_is_immutable():

    joint = create_joint()

    with pytest.raises(FrozenInstanceError):
        joint.name = "Different"