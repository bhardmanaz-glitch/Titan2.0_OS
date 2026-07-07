import pytest

from titan.hardware.prototype import PROTOTYPE_LEG


def test_femur_length():
    assert PROTOTYPE_LEG.femur.length == pytest.approx(0.11628)


def test_tibia_length():
    assert PROTOTYPE_LEG.tibia.length == pytest.approx(0.15875)


def test_total_leg_length():
    assert (
        PROTOTYPE_LEG.femur.length
        + PROTOTYPE_LEG.tibia.length
    ) == pytest.approx(0.27503)


def test_prototype_leg_exists():

    assert PROTOTYPE_LEG.name == "Prototype"


def test_prototype_geometry():

    assert PROTOTYPE_LEG.femur.length == 0.11628
    assert PROTOTYPE_LEG.tibia.length == 0.15875


def test_prototype_joints():

    assert PROTOTYPE_LEG.hip.name == "Hip"
    assert PROTOTYPE_LEG.knee.name == "Knee"