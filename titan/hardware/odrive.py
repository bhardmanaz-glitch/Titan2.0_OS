"""
Titan2_OS

ODrive Hardware Abstraction Layer

This module wraps all communication with one ODrive axis.

Nothing outside this file should ever need to know CAN IDs,
message formats, or ODrive internals.
"""

from dataclasses import dataclass


@dataclass
class ODriveAxis:
    """
    Represents one physical ODrive axis.
    """

    name: str
    axis_id: int

    enabled: bool = False

    position: float = 0.0
    velocity: float = 0.0
    torque: float = 0.0

    encoder_position: float = 0.0
    encoder_velocity: float = 0.0

    error: int = 0

    def enable(self):

        self.enabled = True
        print(f"{self.name} ENABLED")

    def disable(self):

        self.enabled = False
        print(f"{self.name} DISABLED")

    def clear_errors(self):

        self.error = 0
        print(f"{self.name} Errors Cleared")

    def set_position(self, position):

        self.position = position

    def set_velocity(self, velocity):

        self.velocity = velocity

    def set_torque(self, torque):

        self.torque = torque

    def heartbeat(self):

        print(
            f"{self.name}: "
            f"Enabled={self.enabled} "
            f"Pos={self.position:.3f} "
            f"Vel={self.velocity:.3f}"
        )