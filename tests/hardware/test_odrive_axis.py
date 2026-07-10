"""
Titan2_OS

Unit Tests for ODriveAxis
"""

import pytest

from titan.hardware.odrive_axis import ODriveAxis
from titan.hardware.telemetry import Telemetry


# ============================================================
# Fake ODrive Hardware
# ============================================================

class FakeDriver:
    vbus_voltage = 24.5
    ibus = 0.6

    fw_version_major = 0
    fw_version_minor = 6
    fw_version_revision = 11

    thermistor0 = 33.2


class FakeMotor:

    class FOC:
        Iq_measured = 1.8

    foc = FOC()


class FakeAxis:

    motor = FakeMotor()

    pos_estimate = 1.57
    vel_estimate = 2.30

    current_state = "IDLE"

    active_errors = ()
    disarm_reason = None


# ============================================================
# Tests
# ============================================================

def test_create_odrive_axis():

    axis = ODriveAxis(
        serial_number="TEST123",
        axis_index=0,
    )

    assert axis.connected is False


def test_disconnect():

    axis = ODriveAxis(
        serial_number="TEST123",
        axis_index=0,
    )

    # Simulate a connected axis
    axis._connected = True
    axis._driver = FakeDriver()
    axis._axis = FakeAxis()

    axis.disconnect()

    assert axis.connected is False
    assert axis._driver is None
    assert axis._axis is None


def test_refresh_requires_connection():

    axis = ODriveAxis(
        serial_number="TEST123",
        axis_index=0,
    )

    with pytest.raises(RuntimeError):
        axis.refresh()


def test_refresh_returns_telemetry():

    axis = ODriveAxis(
        serial_number="TEST123",
        axis_index=0,
    )

    # Inject fake hardware
    axis._connected = True
    axis._driver = FakeDriver()
    axis._axis = FakeAxis()

    telemetry = axis.refresh()

    assert isinstance(telemetry, Telemetry)

    assert telemetry.position == pytest.approx(1.57)
    assert telemetry.velocity == pytest.approx(2.30)
    assert telemetry.current == pytest.approx(1.8)
    assert telemetry.temperature == pytest.approx(33.2)
    assert telemetry.bus_voltage == pytest.approx(24.5)
    assert telemetry.bus_current == pytest.approx(0.6)

    assert telemetry.active_errors == ()
    assert telemetry.disarm_reason is None