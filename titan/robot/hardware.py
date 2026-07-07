"""
Titan 2.0 Operating System

Titan Hardware Catalog

This module defines the canonical hardware used
throughout Titan2_OS.

There should only ever be one definition of each
physical component.
"""

from ..hardware.motor import Motor
from ..hardware.gearbox import Gearbox
from ..hardware.link import Link

GL40 = Motor(
    manufacturer="Cubemars",
    model="GL40",
)

GL30 = Motor(
    manufacturer="Cubemars",
    model="GL30",
)

HIP_GEARBOX = Gearbox(
    type="Planetary",
    ratio=36.0,
)

KNEE_GEARBOX = Gearbox(
    type="Timing Belt",
    ratio=9.0,
)

FEMUR = Link(
    name="Femur",
    length=0.11628,
)

TIBIA = Link(
    name="Tibia",
    length=0.15875,
)
