"""
Titan 2.0 Operating System

Digital Twin

Motor
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Motor:
    """
    Immutable description of a physical motor.
    """

    name: str

    manufacturer: str | None = None
    model: str | None = None

    max_torque: float | None = None
    max_speed: float | None = None

    voltage: float | None = None
    current_limit: float | None = None

    encoder_cpr: int | None = None

    weight: float | None = None