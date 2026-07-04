"""
Titan2_OS
Unit Tests for Joint Class
"""

from titan.hardware.odrive import ODriveAxis
from titan.hardware.joint import Joint


def create_joint():
    """Create a test joint."""

    motor = ODriveAxis(
        name="Test Motor",
        axis_id=0,
    )

    joint = Joint(
        name="Test Joint",
        actuator=motor,
        gear_ratio=36.0,
        min_angle=-1.4,
        max_angle=0.8,
    )

    return joint


def test_joint_to_motor_conversion():

    joint = create_joint()

    assert joint._joint_to_motor(0.5) == 18.0


def test_motor_to_joint_conversion():

    joint = create_joint()

    assert joint._motor_to_joint(18.0) == 0.5


def test_move_safe_clamps():

    joint = create_joint()

    joint.move_safe(2.0)

    assert joint.angle == 0.8


def test_within_limits():

    joint = create_joint()

    assert joint._within_limits(0.5)

    assert not joint._within_limits(2.0)