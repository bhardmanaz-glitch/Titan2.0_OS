"""
Titan2_OS

Joint Abstraction Layer

A Joint represents one physical robot joint.

It owns an actuator and exposes a clean robotics interface.

Nothing above this layer should know how the actuator works.
"""

from dataclasses import dataclass

from titan.hardware.odrive import ODriveAxis


@dataclass
class Joint:
    """
    Physical robot joint.
    """

    def __init__(
        self,
        name: str,
        actuator,
        gear_ratio: float,
        min_angle: float,
        max_angle: float,
    ):

        self.name = name

        self.actuator = actuator

        self.gear_ratio = gear_ratio

        self.min_angle = min_angle

        self.max_angle = max_angle

        self._angle = 0.0
    enabled: bool = False

    # ----------------------------

    def _joint_to_motor(self, angle):
        return angle * self.gear_ratio
    
    # ----------------------------

    def _motor_to_joint(self, turns):
        return turns / self.gear_ratio
    
    # ------------------------------

    def _within_limits(self, angle):

        return self.min_angle <= angle <= self.max_angle
    
    # ------------------------------

    def _clamp(self, angle):

        return max(
            self.min_angle,
            min(angle, self.max_angle)
        )
    
    # -------------------------------

    def move_raw(self, angle):

        motor_turns = self._joint_to_motor(angle)

        self.actuator.set_position(motor_turns)

        self._angle = angle

        # ------------------------------

    def move_safe(self, angle):

        safe_angle = self._clamp(angle)

        self.move_raw(safe_angle)

        # ------------------------------

    def enable(self):

        self.actuator.enable()

        self.enabled = True

    # ----------------------------

    def disable(self):

        self.actuator.disable()

        self.enabled = False

    # ----------------------------

    def move_to(self, angle):

        if angle < self.min_angle:
            raise ValueError(f"{self.name}: angle below limit")

        if angle > self.max_angle:
            raise ValueError(f"{self.name}: angle above limit")

        motor_position = (
            angle * self.gear_ratio
            + self.zero_offset
        )

        self.actuator.set_position(motor_position)

    # ----------------------------

    def stop(self):

        self.actuator.disable()

    # ----------------------------

    def home(self):

        self.move_safe(0.0)

    # ----------------------------

    @property
    def angle(self):

        return self._motor_to_joint(
            self.actuator.position
        )
    
    @property
    def motor_position(self):

        return self.actuator.position