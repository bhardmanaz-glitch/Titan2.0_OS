"""
Titan 2.0 Operating System

Digital Twin

Foot
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Foot:
    """
    Represents Titan's foot.

    Future versions may include
    contact sensors,
    force sensors,
    compliance,
    and tread geometry.
    """

    radius: float = 0.0