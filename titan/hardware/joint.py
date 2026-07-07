from dataclasses import dataclass

from titan.hardware.actuator import Actuator


@dataclass(slots=True, frozen=True)
class Joint:
    """
    Immutable description of a robot joint.
    """

    name: str

    actuator: Actuator

    min_angle: float

    max_angle: float

    zero_position: float = 0.0