import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.link import Link


def test_create_link():

    femur = Link(
        name="Femur",
        length=0.11628,
    )

    assert femur.name == "Femur"
    assert femur.length == 0.11628


def test_optional_properties():

    femur = Link(
        name="Femur",
        length=0.11628,
        mass=0.45,
        center_of_mass=0.058,
        inertia=0.0012,
    )

    assert femur.mass == 0.45
    assert femur.center_of_mass == 0.058
    assert femur.inertia == 0.0012


def test_default_properties_are_none():

    femur = Link(
        name="Femur",
        length=0.11628,
    )

    assert femur.mass is None
    assert femur.center_of_mass is None
    assert femur.inertia is None


def test_link_is_immutable():

    femur = Link(
        name="Femur",
        length=0.11628,
    )

    with pytest.raises(FrozenInstanceError):
        femur.length = 0.20