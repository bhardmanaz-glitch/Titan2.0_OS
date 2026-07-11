"""
Titan 2.0 Operating System

Actuator Command

Represents a command expressed in actuator space.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ActuatorCommand:
    """
    Desired actuator command.

    Position is expressed in actuator units.
    """

    position: float