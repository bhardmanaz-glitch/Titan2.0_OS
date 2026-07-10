import pytest

from titan.hardware.axis_driver import AxisDriver
from titan.hardware.mock_axis import MockAxis
from titan.hardware.telemetry import Telemetry


def test_mock_axis_is_axis_driver():

    axis = MockAxis()

    assert isinstance(axis, AxisDriver)


def test_mock_axis_starts_disconnected():

    axis = MockAxis()

    assert axis.connected is False


def test_connect():

    axis = MockAxis()

    axis.connect()

    assert axis.connected is True


def test_disconnect():

    axis = MockAxis()

    axis.connect()
    axis.disconnect()

    assert axis.connected is False


def test_default_position():

    axis = MockAxis()

    assert axis.position == 0.0


def test_default_velocity():

    axis = MockAxis()

    assert axis.velocity == 0.0


def test_default_current():

    axis = MockAxis()

    assert axis.current == 0.0


def test_default_bus_voltage():

    axis = MockAxis()

    assert axis.bus_voltage == 24.0


def test_default_bus_current():

    axis = MockAxis()

    assert axis.bus_current == 0.0


def test_default_temperature():

    axis = MockAxis()

    assert axis.temperature == 25.0


def test_default_axis_state():

    axis = MockAxis()

    assert axis.axis_state == "IDLE"


def test_default_serial_number():

    axis = MockAxis()

    assert axis.serial_number == "MOCK"


def test_default_firmware():

    axis = MockAxis()

    assert axis.firmware_version == "0.0"


def test_default_errors():

    axis = MockAxis()

    assert axis.active_errors == []


def test_default_disarm_reason():

    axis = MockAxis()

    assert axis.disarm_reason is None


# --------------------------------------------------------
# set_state()
# --------------------------------------------------------

def test_set_position():

    axis = MockAxis()

    axis.set_state(position=1.57)

    assert axis.position == 1.57


def test_set_velocity():

    axis = MockAxis()

    axis.set_state(velocity=5.0)

    assert axis.velocity == 5.0


def test_set_current():

    axis = MockAxis()

    axis.set_state(current=2.3)

    assert axis.current == 2.3


def test_set_temperature():

    axis = MockAxis()

    axis.set_state(temperature=48.5)

    assert axis.temperature == 48.5


def test_set_bus_voltage():

    axis = MockAxis()

    axis.set_state(bus_voltage=25.2)

    assert axis.bus_voltage == 25.2


def test_set_bus_current():

    axis = MockAxis()

    axis.set_state(bus_current=4.1)

    assert axis.bus_current == 4.1


def test_set_axis_state():

    axis = MockAxis()

    axis.set_state(axis_state="CLOSED_LOOP_CONTROL")

    assert axis.axis_state == "CLOSED_LOOP_CONTROL"


def test_set_errors():

    axis = MockAxis()

    axis.set_state(active_errors=["OVERTEMP"])

    assert axis.active_errors == ["OVERTEMP"]


def test_set_disarm_reason():

    axis = MockAxis()

    axis.set_state(disarm_reason="OVERTEMP")

    assert axis.disarm_reason == "OVERTEMP"


def test_set_multiple_values():

    axis = MockAxis()

    axis.set_state(
        position=1.2,
        velocity=3.5,
        current=4.6,
        temperature=40.0,
        bus_voltage=25.0,
        bus_current=2.8,
        axis_state="CLOSED_LOOP_CONTROL",
        active_errors=["TEST"],
        disarm_reason="TEST",
    )

    assert axis.position == 1.2
    assert axis.velocity == 3.5
    assert axis.current == 4.6
    assert axis.temperature == 40.0
    assert axis.bus_voltage == 25.0
    assert axis.bus_current == 2.8
    assert axis.axis_state == "CLOSED_LOOP_CONTROL"
    assert axis.active_errors == ["TEST"]
    assert axis.disarm_reason == "TEST"


def test_set_state_returns_self():

    axis = MockAxis()

    returned = axis.set_state(position=5.0)

    assert returned is axis

def test_refresh_returns_telemetry():

    axis = MockAxis()

    snapshot = axis.refresh()

    assert isinstance(snapshot, Telemetry)


def test_refresh_default_values():

    axis = MockAxis()

    t = axis.refresh()

    assert t.position == 0.0
    assert t.velocity == 0.0
    assert t.current == 0.0
    assert t.temperature == 25.0
    assert t.bus_voltage == 24.0
    assert t.bus_current == 0.0
    assert t.axis_state == "IDLE"
    assert t.active_errors == ()
    assert t.disarm_reason is None


def test_refresh_after_set_state():

    axis = MockAxis()

    axis.set_state(
        position=1.57,
        velocity=4.2,
        current=3.1,
        temperature=41.0,
        bus_voltage=23.8,
        bus_current=2.6,
        axis_state="CLOSED_LOOP_CONTROL",
        active_errors=["NONE"],
        disarm_reason=None,
    )

    t = axis.refresh()

    assert t.position == 1.57
    assert t.velocity == 4.2
    assert t.current == 3.1
    assert t.temperature == 41.0
    assert t.bus_voltage == 23.8
    assert t.bus_current == 2.6
    assert t.axis_state == "CLOSED_LOOP_CONTROL"
    assert t.active_errors == ("NONE",)
    assert t.disarm_reason is None