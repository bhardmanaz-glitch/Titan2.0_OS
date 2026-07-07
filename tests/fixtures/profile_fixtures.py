import pytest

from titan.motion.profiles import (
    LinearProfile,
    TrapezoidalProfile,
)


@pytest.fixture
def linear_profile():
    return LinearProfile()


@pytest.fixture
def trapezoidal_profile():
    return TrapezoidalProfile()