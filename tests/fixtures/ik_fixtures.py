import pytest

from titan.hardware.prototype import PROTOTYPE_LEG
from titan.kinematics.inverse_kinematics import InverseKinematics


@pytest.fixture
def inverse_kinematics():
    return InverseKinematics(
        PROTOTYPE_LEG,
    )