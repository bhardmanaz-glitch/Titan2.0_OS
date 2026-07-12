import pytest

from titan.hardware.actuator_mapper import ActuatorMapper


@pytest.fixture
def hip_mapper():
    return ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.0,
    )


@pytest.fixture
def knee_mapper():
    return ActuatorMapper(
        gear_ratio=9,
        sign=1,
        zero_offset=0.0,
    )


# Backward compatibility
@pytest.fixture
def actuator_mapper(
    hip_mapper,
):
    return hip_mapper