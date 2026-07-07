import pytest
from dataclasses import FrozenInstanceError

from titan.hardware.gearbox import Gearbox


def test_create_gearbox():

    gearbox = Gearbox(
        name="Hip Planetary",
        ratio=36.0,
    )

    assert gearbox.ratio == 36.0


def test_gearbox_is_immutable():

    gearbox = Gearbox(
        name="Hip Planetary",
        ratio=36.0,
    )

    with pytest.raises(FrozenInstanceError):
        gearbox.ratio = 40.0