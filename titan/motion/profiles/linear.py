from titan.motion.profiles.base import MotionProfile
from titan.motion.trajectory import MotionPoint


class LinearProfile(MotionProfile):
    """
    Simple constant-velocity linear interpolation.
    """

    def generate(self, plan):

        trajectory = []

        for i in range(plan.steps + 1):

            alpha = i / plan.steps

            position = (
                plan.start
                + plan.direction
                * plan.distance
                * alpha
            )

            point = MotionPoint(
                position=position,
                velocity=plan.max_velocity * plan.direction,
                acceleration=0.0,
                time=i * plan.dt,
                dt=plan.dt,
            )

            trajectory.append(point)

        return trajectory