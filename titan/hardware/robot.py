"""
Titan 2.0 Operating System

Digital Twin

Robot
"""

from dataclasses import dataclass

from titan.hardware.leg import Leg


@dataclass(slots=True, frozen=True)
class Robot:
    """
    Immutable robot hardware definition.

    A robot consists of four immutable legs.
    """

    left_front: Leg

    right_front: Leg

    left_rear: Leg

    right_rear: Leg