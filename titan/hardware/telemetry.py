"""
Titan 2.0 Operating System

Telemetry

Immutable snapshot of one actuator at one instant in time.
"""

from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class Telemetry:
    """
    Immutable snapshot of actuator state.
    """

    position: float
    velocity: float
    current: float

    temperature: float

    bus_voltage: float
    bus_current: float

    axis_state: str

    active_errors: tuple[str, ...] = field(default_factory=tuple)

    disarm_reason: str | None = None