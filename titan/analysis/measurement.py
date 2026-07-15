"""
Titan 2.0 Operating System

Motion Measurement

Immutable record of one actuator measurement.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MotionMeasurement:
    """
    One measured actuator movement.
    """

    target: float
    actual: float
    error: float