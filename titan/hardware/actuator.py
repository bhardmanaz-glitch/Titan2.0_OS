"""
Titan 2.0 Operating System

Digital Twin

Actuator
"""

from dataclasses import dataclass

from titan.hardware.motor import Motor
from titan.hardware.gearbox import Gearbox


@dataclass(slots=True, frozen=True)
class Actuator:
    """
    Immutable actuator assembly.

    An actuator consists of one motor and one gearbox.
    """

    motor: Motor

    gearbox: Gearbox

    @property
    def ratio(self) -> float:
        return self.gearbox.ratio