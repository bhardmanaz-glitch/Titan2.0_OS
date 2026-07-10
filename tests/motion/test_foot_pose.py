import pytest
from dataclasses import FrozenInstanceError

from titan.motion.foot_pose import FootPose


def test_create_foot_pose():

    pose = FootPose(
        x=.100,
        y=-.150,
    )

    assert pose.x == .100
    assert pose.y == -.150


def test_foot_pose_is_frozen():

    pose = FootPose(
        x=.100,
        y=-.150,
    )

    with pytest.raises(FrozenInstanceError):
        pose.x = .50


def test_foot_pose_equality():

    a = FootPose(.100, -.150)
    b = FootPose(.100, -.150)

    assert a == b