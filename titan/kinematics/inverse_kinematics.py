import math

from titan.hardware.leg import Leg
from titan.motion.foot_pose import FootPose
from titan.motion.joint_pose import JointPose


class InverseKinematics:

    """
    Solves 2-link planar inverse kinematics for a Titan leg.
    """

    def __init__(self, leg: Leg):

        self.leg = leg

    @property
    def femur_length(self):

        return self.leg.femur.length


    @property
    def tibia_length(self):

        return self.leg.tibia.length
    
    @property
    def max_reach(self):

        return self.femur_length + self.tibia_length


    @property
    def min_reach(self):

        return abs(
            self.femur_length
            - self.tibia_length
        )


    @property
    def hip_limits(self):

        return (
            self.leg.hip.min_angle,
            self.leg.hip.max_angle,
        )


    @property
    def knee_limits(self):

        return (
            self.leg.knee.min_angle,
            self.leg.knee.max_angle,
        )

    def solve(
        self,
        pose: FootPose,
    ) -> JointPose:

        r = math.hypot(
            pose.x,
            pose.y,
        )
      

        if r > self.max_reach:
            raise ValueError(
                "Foot position is outside reachable workspace."
            )

        if r < self.min_reach:
            raise ValueError(
                "Foot position is inside unreachable workspace."
            )

        cos_knee = (
            self.femur_length**2
            + self.tibia_length**2
            - r**2
        ) / (
            2
            * self.femur_length
            * self.tibia_length
        )
        cos_knee = max(-1.0, min(1.0, cos_knee))
        interior = math.acos(cos_knee)

        knee = math.pi - interior

        cos_alpha = (
            self.femur_length**2
            + r**2
            - self.tibia_length**2
        ) / (
            2
            * self.femur_length
            * r
        )

        cos_alpha = max(-1.0, min(1.0, cos_alpha))
        alpha = math.acos(cos_alpha)

        foot_angle = math.atan2(
            pose.y,
            pose.x,
        )

        hip = foot_angle - alpha

        return JointPose(
            hip=hip,
            knee=knee,
        )


    
        