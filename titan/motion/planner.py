from titan.motion.trajectory import MotionPlan, Trajectory
from titan.motion.profiles import LinearProfile


class TrajectoryPlanner:
    """
    Creates MotionPlans and delegates trajectory generation
    to the selected MotionProfile.
    """

    def __init__(
        self,
        profile=None,
        max_velocity=0.5,
        max_acceleration=1.0,
    ):
        
        if isinstance(profile, str):
            raise TypeError(
                "TrajectoryPlanner now expects a MotionProfile object.\n"
                "Use LinearProfile() instead of 'linear'."
            )

        self.motion_profile = profile or LinearProfile()
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration

    def set_profile(self, profile):
        if isinstance(profile, str):
            raise TypeError(
                "TrajectoryPlanner now expects a MotionProfile object.\n"
                "Use LinearProfile() instead of 'linear'."
            )

        self.motion_profile = profile

    def plan(
        self,
        start,
        end,
        duration=None,
        dt=0.02,
    ):
        """
        Compute all motion parameters without generating
        trajectory points.
        """

        distance = end - start

        direction = 1 if distance >= 0 else -1

        distance = abs(distance)

        accel_time = self.max_velocity / self.max_acceleration
        
        accel_distance = (
            0.5
            * self.max_acceleration
            * accel_time**2
        )

        decel_time = accel_time
        decel_distance = accel_distance

        if accel_distance + decel_distance > distance:
            # -----------------------------
            # Triangular profile
            # -----------------------------
            from math import sqrt

            accel_distance = distance / 2
            decel_distance = distance / 2
            cruise_distance = 0.0

            accel_time = sqrt(
                2 * accel_distance / self.max_acceleration
            )

            decel_time = accel_time
            cruise_time = 0.0

            peak_velocity = (
                self.max_acceleration * accel_time
            )

            duration = (
                accel_time
                + decel_time
            )

        else:
            # -----------------------------
            # Trapezoidal profile
            # -----------------------------
            cruise_distance = (
                distance
                - accel_distance
                - decel_distance
            )

            cruise_time = (
                cruise_distance
                / self.max_velocity
            )

            duration = (
                accel_time
                + cruise_time
                + decel_time
            )

            peak_velocity = self.max_velocity

        steps = max(
            1,
            round(duration / dt)
        )

        return MotionPlan(
    start=start,
    end=end,

    distance=distance,
    direction=direction,

    duration=duration,

    max_velocity=peak_velocity,
    max_acceleration=self.max_acceleration,

    accel_time=accel_time,
    cruise_time=cruise_time,
    decel_time=decel_time,

    accel_distance=accel_distance,
    cruise_distance=cruise_distance,
    decel_distance=decel_distance,

    steps=steps,
    dt=dt,
)
    
    def _create_motion_plan(
        self,
        start,
        end,
        duration=None,
        dt=0.02,
    ):
        """
        Compute all motion parameters without generating trajectory points.
        """

        distance = end - start

        direction = 1 if distance >= 0 else -1

        distance = abs(distance)

        accel_time = self.max_velocity / self.max_acceleration

        accel_distance = (
            0.5
            * self.max_acceleration
            * accel_time**2
        )

        decel_time = accel_time

        decel_distance = accel_distance

        if accel_distance + decel_distance > distance:
            accel_distance = distance / 2.0
            decel_distance = distance / 2.0

            accel_time = (
                2.0
                * accel_distance
                / self.max_acceleration
            ) ** 0.5

            decel_time = accel_time

            cruise_distance = 0.0
            cruise_time = 0.0

            max_velocity = (
                self.max_acceleration
                * accel_time
            )

        else:
            cruise_distance = (
                distance
                - accel_distance
                - decel_distance
            )

            max_velocity = self.max_velocity

            cruise_time = (
                cruise_distance
                / max_velocity
            )

        if duration is None:
            duration = (
                accel_time
                + cruise_time
                + decel_time
            )

        steps = int(round(duration / dt)) + 1

        return MotionPlan(
            start=start,
            end=end,

            distance=distance,
            direction=direction,

            duration=duration,

            max_velocity=max_velocity,
            max_acceleration=self.max_acceleration,

            accel_time=accel_time,
            cruise_time=cruise_time,
            decel_time=decel_time,

            accel_distance=accel_distance,
            cruise_distance=cruise_distance,
            decel_distance=decel_distance,

            steps=steps,
            dt=dt,
        )
    
    def generate(
        self,
        start,
        end,
        duration=None,
        dt=0.02,
    ):
        """
        Generate a complete trajectory using the
        currently selected MotionProfile.
        """

        motion_plan = self._create_motion_plan(
            start=start,
            end=end,
            duration=duration,
            dt=dt,
        )

        points = self.motion_profile.generate(motion_plan)

        return Trajectory(
            points=points,
            duration=motion_plan.duration,
            distance=motion_plan.distance,
            dt=motion_plan.dt,
            start=motion_plan.start,
            end=motion_plan.end,
        )