"""
Titan 2.0 Operating System

Actuator Mapper

Converts joint-space commands into actuator-space commands.
"""

import math

from titan.hardware.actuator_command import ActuatorCommand


class ActuatorMapper:

    def __init__(
        self,
        gear_ratio: float,
        sign: int = 1,
        zero_offset: float = 0.0,
    ):
        self.gear_ratio = gear_ratio
        self.sign = sign
        self.zero_offset = zero_offset

    def map(
        self,
        joint_position: float,
    ) -> ActuatorCommand:

        joint_turns = (
            joint_position
            / (2 * math.pi)
        )

        motor_turns = (
            joint_turns
            * self.gear_ratio
            * self.sign
        )

        return ActuatorCommand(
            position=(
                self.zero_offset
                + motor_turns
            )   
        )