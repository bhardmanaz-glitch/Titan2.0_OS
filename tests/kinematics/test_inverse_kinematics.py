import pytest

from titan.hardware.prototype import PROTOTYPE_LEG
from titan.kinematics.inverse_kinematics import InverseKinematics
from titan.motion.foot_pose import FootPose
from titan.motion.joint_pose import JointPose


def test_create_inverse_kinematics():

    ik = InverseKinematics(
    leg=PROTOTYPE_LEG,
    )

def test_rejects_pose_too_far():

    ik = InverseKinematics(
    leg=PROTOTYPE_LEG,
    )

    max_reach = ik.max_reach

    pose = FootPose(
        x=max_reach + 0.001,
        y=0.0,
    )

    with pytest.raises(ValueError):
        ik.solve(pose)

def test_rejects_pose_too_close():

    ik = InverseKinematics(
    leg=PROTOTYPE_LEG,
    )

    max_reach = ik.max_reach

    pose = FootPose(
        x=max_reach + 0.001,
        y=0.0,
    )

    with pytest.raises(ValueError):
        ik.solve(pose)

@property
def max_reach(self):

    return (
        self.femur_length
        + self.tibia_length
    )


@property
def min_reach(self):

    return abs(
        self.femur_length
        - self.tibia_length
    )

def test_accepts_pose_at_maximum_reach():

    ik = InverseKinematics(
        leg=PROTOTYPE_LEG,
    )

    pose = FootPose(
        x=ik.max_reach,
        y=0.0,
    )

    joints = ik.solve(pose)

    assert isinstance(joints, JointPose)

def test_accepts_pose_at_minimum_reach():

    ik = InverseKinematics(
        leg=PROTOTYPE_LEG,
    )

    pose = FootPose(
        x=ik.min_reach,
        y=0.0,
    )

    joints = ik.solve(pose)

    assert isinstance(joints, JointPose)


