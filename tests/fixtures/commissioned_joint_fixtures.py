import pytest

from titan.hardware.actuator_mapper import (
    ActuatorMapper,
)

from titan.hardware.commissioned_joint import (
    CommissionedJoint,
)

from titan.hardware.mock_axis import (
    MockAxis,
)

from titan.hardware.prototype import (
    PROTOTYPE_LEG,
    PROTOTYPE_ROBOT,
)

@pytest.fixture
def commissioned_joint(
    actuator_mapper,
):
    """
    Backward-compatible fixture used by single-joint executor tests.
    """

    return CommissionedJoint(
        joint=PROTOTYPE_LEG.hip,
        driver=MockAxis(),
        mapper=actuator_mapper,
    )

@pytest.fixture
def left_front_hip_joint(
    hip_mapper,
):

   return CommissionedJoint(
        joint=PROTOTYPE_ROBOT.left_front.hip,
        driver=MockAxis(),
        mapper=hip_mapper,
    )

@pytest.fixture
def left_front_knee_joint(
    knee_mapper,
):

    return CommissionedJoint(
        joint=PROTOTYPE_ROBOT.left_front.knee,
        driver=MockAxis(),
        mapper=knee_mapper,
    )