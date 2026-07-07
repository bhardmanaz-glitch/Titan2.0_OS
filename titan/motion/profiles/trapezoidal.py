from titan.motion.profiles.base import MotionProfile
from titan.motion.trajectory import MotionPoint


class TrapezoidalProfile(MotionProfile):
    """
    Generates a trapezoidal (or triangular) velocity profile
    from a MotionPlan.
    """

    def generate(self, plan):

        trajectory = []

        for i in range(plan.steps + 1):

            t = min(i * plan.dt, plan.duration)

            # ------------------------------------
            # Acceleration Phase
            # ------------------------------------

            if t <= plan.accel_time:

                acceleration = plan.max_acceleration

                velocity = acceleration * t

                position = (
                    0.5
                    * acceleration
                    * t**2
                )

            # ------------------------------------
            # Cruise Phase
            # ------------------------------------

            elif t <= plan.accel_time + plan.cruise_time:

                acceleration = 0.0

                velocity = plan.max_velocity

                cruise_elapsed = (
                    t - plan.accel_time
                )

                position = (
                    plan.accel_distance
                    + velocity * cruise_elapsed
                )

            # ------------------------------------
            # Deceleration Phase
            # ------------------------------------

            else:

                decel_elapsed = (
                    t
                    - plan.accel_time
                    - plan.cruise_time
                )

                acceleration = -plan.max_acceleration

                velocity = (
                    plan.max_velocity
                    - plan.max_acceleration
                    * decel_elapsed
                )

                position = (
                    plan.accel_distance
                    + plan.cruise_distance
                    + plan.max_velocity
                    * decel_elapsed
                    - 0.5
                    * plan.max_acceleration
                    * decel_elapsed**2
                )

            trajectory.append(

                MotionPoint(
                    position=(
                        plan.start
                        + plan.direction
                        * position
                    ),

                    velocity=(
                        plan.direction
                        * velocity
                    ),

                    acceleration=(
                        plan.direction
                        * acceleration
                    ),

                    time=t,
                    dt=plan.dt,
                )

            )

        return trajectory