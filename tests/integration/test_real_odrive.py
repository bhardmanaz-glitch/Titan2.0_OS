"""
Integration test for a real ODrive S1.

Requires:
    • Raspberry Pi
    • ODrive connected over USB
    • Powered motor

This test is NOT intended to run on Windows.
"""

import pytest

odrive = pytest.importorskip("odrive")

from titan.hardware.odrive_axis import ODriveAxis
from titan.hardware.telemetry import Telemetry

def test_connect_and_refresh():

    axis = ODriveAxis(axis_index=0)

    axis.connect()

    telemetry = axis.refresh()

    assert isinstance(telemetry, Telemetry)

    assert axis.connected

    axis.disconnect()

    assert not axis.connected

    print()

    print("Telemetry")
    print("----------------------------")
    print(f"Position      : {telemetry.position}")
    print(f"Velocity      : {telemetry.velocity}")
    print(f"Current       : {telemetry.current}")
    print(f"Temperature   : {telemetry.temperature}")
    print(f"Bus Voltage   : {telemetry.bus_voltage}")
    print(f"Bus Current   : {telemetry.bus_current}")
    print(f"Axis State    : {telemetry.axis_state}")
    print(f"Errors        : {telemetry.active_errors}")
    print(f"Disarm Reason : {telemetry.disarm_reason}")