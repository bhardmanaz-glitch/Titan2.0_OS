import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.motor import Motor


def test_create_motor():

    motor = Motor(
        name="Cubemars GL40",
    )

    assert motor.name == "Cubemars GL40"


def test_motor_is_immutable():
    motor = Motor(name="Cubemars GL40")

    with pytest.raises(FrozenInstanceError):
        motor.name = "Different Motor"
        pass