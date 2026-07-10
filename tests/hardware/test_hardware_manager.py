from titan.hardware.hardware_manager import HardwareManager
from titan.hardware.mock_axis import MockAxis


def test_manager_starts_empty():

    manager = HardwareManager()

    assert manager.axes == {}


def test_add_axis():

    manager = HardwareManager()

    axis = MockAxis()

    manager.add_axis("hip", axis)

    assert "hip" in manager.axes
    assert manager.axes["hip"] is axis


def test_connect_all():

    manager = HardwareManager()

    a = MockAxis()
    b = MockAxis()

    manager.add_axis("hip", a)
    manager.add_axis("knee", b)

    manager.connect()

    assert a.connected
    assert b.connected


def test_disconnect_all():

    manager = HardwareManager()

    a = MockAxis()
    b = MockAxis()

    manager.add_axis("hip", a)
    manager.add_axis("knee", b)

    manager.connect()
    manager.disconnect()

    assert not a.connected
    assert not b.connected


def test_refresh_all():

    manager = HardwareManager()

    a = MockAxis()
    b = MockAxis()

    manager.add_axis("hip", a)
    manager.add_axis("knee", b)

    telemetry = manager.refresh()

    assert len(telemetry) == 2