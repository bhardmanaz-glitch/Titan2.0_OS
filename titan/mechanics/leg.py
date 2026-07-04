"""
Titan 2.0 Operating System
Leg Mechanism

A Leg converts desired foot positions into joint motions.

Author:
Titan Robotics Team
"""

from titan.hardware.joint import Joint


class Leg:
    """
    Two degree-of-freedom robotic leg.
    """

    def __init__(
        self,
        name: str,
        hip: Joint,
        knee: Joint,
        thigh_length: float,
        shin_length: float,
    ):

        self.name = name

        self.hip = hip
        self.knee = knee

        # SI Units (meters)

        self.thigh_length = thigh_length
        self.shin_length = shin_length

        # Current foot position

        self.x = 0.0
        self.y = -(thigh_length + shin_length)

    def enable(self):

        self.hip.enable()
        self.knee.enable()


    def disable(self):

        self.hip.disable()
        self.knee.disable()

    def print_status(self):

        print()

        print("==========", self.name, "==========")

        print("Foot X:", self.x)

        print("Foot Y:", self.y)

        print("Hip Angle:", self.hip.angle)

        print("Knee Angle:", self.knee.angle)

        print("==============================")

        print()

    def get_position(self):

        return self.x, self.y