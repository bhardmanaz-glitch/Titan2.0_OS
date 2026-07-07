"""
Titan 2.0 Operating System

Digital Twin

Gearbox
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Gearbox:
    """
    Immutable description of a gearbox.
    """

    name: str

    ratio: float

    efficiency: float = 1.0

    backlash: float = 0.0

    weight: float | None = None