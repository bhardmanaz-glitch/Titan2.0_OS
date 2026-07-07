import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.motor import Motor
from titan.hardware.gearbox import Gearbox
from titan.hardware.actuator import Actuator


def test_create_actuator():

    motor = Motor(
        name="Cubemars GL40",
    )

    gearbox = Gearbox(
        name="Hip Planetary",
        ratio=36.0,
    )

    actuator = Actuator(
        motor=motor,
        gearbox=gearbox,
    )

    assert actuator.motor is motor
    assert actuator.gearbox is gearbox


def test_actuator_ratio():

    actuator = Actuator(
        motor=Motor(name="GL40"),
        gearbox=Gearbox(
            name="Planetary",
            ratio=36.0,
        ),
    )

    assert actuator.ratio == 36.0


def test_actuator_is_immutable():

    actuator = Actuator(
        motor=Motor(name="GL40"),
        gearbox=Gearbox(
            name="Planetary",
            ratio=36.0,
        ),
    )

    with pytest.raises(FrozenInstanceError):
        actuator.gearbox = None