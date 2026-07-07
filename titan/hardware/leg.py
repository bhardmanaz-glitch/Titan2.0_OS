"""
Titan2_OS

Leg Digital Twin

A Leg is a collection of physical hardware.

It owns:
    - Hip Joint
    - Knee Joint
    - Femur
    - Tibia
    - Foot

The Leg contains no motion logic.

Inverse kinematics, trajectory generation, and gait planning
are handled elsewhere.
"""

from dataclasses import dataclass

from titan.hardware.joint import Joint
from titan.hardware.link import Link
from titan.hardware.foot import Foot


@dataclass(slots=True, frozen=True)
class Leg:
    """
    Physical robot leg.
    """

    name: str

    hip: Joint
    knee: Joint

    femur: Link
    tibia: Link

    foot: Foot