import pytest

from titan.hardware.axis_driver import AxisDriver


def test_axis_driver_is_abstract():

    with pytest.raises(TypeError):
        AxisDriver()


def test_connect_method_exists():
    assert hasattr(AxisDriver, "connect")


def test_refresh_method_exists():
    assert hasattr(AxisDriver, "refresh")