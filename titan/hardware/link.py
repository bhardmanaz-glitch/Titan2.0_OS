"""
Titan 2.0 Operating System

Digital Twin

Structural Link
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Link:
    """
    Represents a rigid structural member.

    Examples
    --------
    Femur
    Tibia
    """

    name: str

    length: float

    mass: float | None = None

    center_of_mass: float | None = None

    inertia: float | None = None