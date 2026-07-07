import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.leg import Leg
from titan.hardware.joint import Joint
from titan.hardware.link import Link
from titan.hardware.foot import Foot
from titan.hardware.actuator import Actuator
from titan.hardware.motor import Motor
from titan.hardware.gearbox import Gearbox


def create_joint(name):

    actuator = Actuator(
        motor=Motor(name="Motor"),
        gearbox=Gearbox(
            name="Gearbox",
            ratio=1.0,
        ),
    )

    return Joint(
        name=name,
        actuator=actuator,
        min_angle=-1.0,
        max_angle=1.0,
    )


def test_create_leg():

    hip = create_joint("Hip")
    knee = create_joint("Knee")

    femur = Link(
        name="Femur",
        length=0.11628,
    )

    tibia = Link(
        name="Tibia",
        length=0.15875,
    )

    foot = Foot()

    leg = Leg(
        name="Left Front",
        hip=hip,
        knee=knee,
        femur=femur,
        tibia=tibia,
        foot=foot,
    )

    assert leg.name == "Left Front"


def test_components_are_preserved():

    hip = create_joint("Hip")
    knee = create_joint("Knee")

    femur = Link(
        name="Femur",
        length=0.11628,
    )

    tibia = Link(
        name="Tibia",
        length=0.15875,
    )

    foot = Foot()

    leg = Leg(
        name="Left Front",
        hip=hip,
        knee=knee,
        femur=femur,
        tibia=tibia,
        foot=foot,
    )

    assert leg.hip is hip
    assert leg.knee is knee
    assert leg.femur is femur
    assert leg.tibia is tibia
    assert leg.foot is foot


def test_leg_is_immutable():

    hip = create_joint("Hip")
    knee = create_joint("Knee")

    femur = Link(
        name="Femur",
        length=0.11628,
    )

    tibia = Link(
        name="Tibia",
        length=0.15875,
    )

    foot = Foot()

    leg = Leg(
        name="Left Front",
        hip=hip,
        knee=knee,
        femur=femur,
        tibia=tibia,
        foot=foot,
    )

    with pytest.raises(FrozenInstanceError):
        leg.name = "Right Front"