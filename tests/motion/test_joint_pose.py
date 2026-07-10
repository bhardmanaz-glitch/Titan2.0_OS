from dataclasses import FrozenInstanceError

import pytest

from titan.motion.joint_pose import JointPose


def test_create_joint_pose():

    pose = JointPose(
        hip=15.0,
        knee=40.0,
    )

    assert pose.hip == 15.0
    assert pose.knee == 40.0


def test_joint_pose_is_frozen():

    pose = JointPose(
        hip=15.0,
        knee=40.0,
    )

    with pytest.raises(FrozenInstanceError):
        pose.hip = 20.0


def test_joint_pose_equality():

    a = JointPose(10.0, 20.0)
    b = JointPose(10.0, 20.0)

    assert a == b
    