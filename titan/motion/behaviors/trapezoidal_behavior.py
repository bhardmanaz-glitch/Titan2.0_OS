import math

from titan.motion.behaviors import MotionBehavior
from titan.motion.foot_pose import FootPose
from titan.motion.trajectory import MotionPoint, Trajectory


class TrapezoidalBehavior(MotionBehavior[FootPose]):

    def generate(
        self,
        start: FootPose,
        end: FootPose,
        duration: float,
        dt: float,
    ) -> Trajectory[FootPose]:
        
        if duration < 0:
            raise ValueError("Duration must be non-negative.")

        if dt <= 0:
            raise ValueError("dt must be greater than zero.")
        
        self._validate_inputs(
            start,
            end,
            duration,
            dt,
        )

        if duration == 0:
            return self._generate_single_point_trajectory(start)

    def _validate_inputs(
        self,
        start: FootPose,
        end: FootPose,
        duration: float,
        dt: float,
    ) -> None:
        if duration < 0:
            raise ValueError("duration must be non-negative")

        if dt <= 0:
            raise ValueError("dt must be greater than zero")
        
        if duration == 0 and start != end:
            raise ValueError(
                "Cannot move between different poses in zero time."
            )
        
    def _generate_single_point_trajectory(
        self,
        pose: FootPose,
    ) -> Trajectory[FootPose]:
        point = MotionPoint(
            position=pose,
            velocity=0.0,
            acceleration=0.0,
            time=0.0,
            dt=0.0,
        )

        return Trajectory(
            points=[point],
            duration=0.0,
            distance=0.0,
            dt=0.0,
            start=pose,
            end=pose,
        )

    def _generate_sample_times(
        self,
        duration: float,
        dt: float,
    ) -> tuple[float, ...]:
        """
        Generate monotonically increasing sample timestamps.

        The returned timestamps always:

        - start at 0.0
        - end at duration
        - never exceed duration
        - never duplicate the endpoint
        """

        sample_count = math.floor(duration / dt)

        times = tuple(
            index * dt
            for index in range(sample_count + 1)
        )

        if math.isclose(times[-1], duration):
            return times

        return (*times, duration)
    
    def _evaluate_profile(
        self,
        time: float,
        duration: float,
    ) -> float:
        """
        Evaluate the normalized progress of the motion profile.

        Returns a value in the range [0.0, 1.0].
        """

        return time / duration
    
    def _interpolate_pose(
        self,
        start: FootPose,
        end: FootPose,
        progress: float,
    ) -> FootPose:
        """
        Linearly interpolate between two Cartesian foot poses.
        """

        return FootPose(
            x=start.x + (end.x - start.x) * progress,
            y=start.y + (end.y - start.y) * progress,
        )