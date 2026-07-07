import pytest

from titan.kinematics.ik import IKSolver


@pytest.fixture
def ik_solver():
    return IKSolver()