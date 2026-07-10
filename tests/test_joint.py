"""
Titan2_OS

Unit Tests for Joint
"""

import pytest
from dataclasses import FrozenInstanceError
from titan.hardware.joint import Joint
from titan.hardware.mock_axis import MockAxis


def create_joint():

    actuator = MockAxis()

    return Joint(
        name="lf_hfe",
        actuator=actuator,
        min_angle=-1.4,
        max_angle=0.8,
    )


def test_joint_creation():

    joint = create_joint()

    assert joint.name == "lf_hfe"

    assert joint.min_angle == -1.4

    assert joint.max_angle == 0.8


def test_zero_position_defaults_to_zero():

    joint = create_joint()

    assert joint.zero_position == 0.0


    with pytest.raises(FrozenInstanceError):
        joint.name = "changed"