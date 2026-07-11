import pytest

from titan.hardware.actuator_mapper import ActuatorMapper


def test_create_mapper():

    mapper = ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.188,
    )

    assert mapper.gear_ratio == 36
    assert mapper.sign == 1
    assert mapper.zero_offset == pytest.approx(
        0.188
    )

def test_zero_angle_returns_zero_offset():

    mapper = ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.188,
    )

    command = mapper.map(0.0)

    assert command.position == pytest.approx(
        0.188
    )

import math

def test_half_revolution():

    mapper = ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.188,
    )

    command = mapper.map(math.pi)

    assert command.position == pytest.approx(
        18.188
    )

def test_negative_sign_reverses_direction():

    mapper = ActuatorMapper(
        gear_ratio=36,
        sign=-1,
        zero_offset=0.188,
    )

    command = mapper.map(math.pi)

    assert command.position == pytest.approx(
        -17.812
    )

def test_gear_ratio_changes_output():

    small = ActuatorMapper(
        gear_ratio=9,
        sign=1,
        zero_offset=0.0,
    )

    large = ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.0,
    )

    assert (
        large.map(math.pi).position
        ==
        pytest.approx(
            4 * small.map(math.pi).position
        )
    )

