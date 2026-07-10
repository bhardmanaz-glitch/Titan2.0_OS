import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.telemetry import Telemetry


def test_create_telemetry():

    telemetry = Telemetry(
        position=1.0,
        velocity=2.0,
        current=3.0,
        temperature=25.0,
        bus_voltage=24.0,
        bus_current=1.5,
        axis_state="IDLE",
        active_errors=(),
        disarm_reason=None,
    )

    assert telemetry.position == 1.0
    assert telemetry.velocity == 2.0
    assert telemetry.current == 3.0


def test_default_error_tuple():

    telemetry = Telemetry(
        position=0.0,
        velocity=0.0,
        current=0.0,
        temperature=25.0,
        bus_voltage=24.0,
        bus_current=0.0,
        axis_state="IDLE",
        active_errors=(),
        disarm_reason=None,
    )

    assert telemetry.active_errors == ()


def test_telemetry_is_immutable():

    telemetry = Telemetry(
        position=0.0,
        velocity=0.0,
        current=0.0,
        temperature=25.0,
        bus_voltage=24.0,
        bus_current=0.0,
        axis_state="IDLE",
        active_errors=(),
        disarm_reason=None,
    )

    with pytest.raises(FrozenInstanceError):
        telemetry.position = 5.0