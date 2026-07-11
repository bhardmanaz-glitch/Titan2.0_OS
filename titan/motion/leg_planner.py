"""
Titan 2.0 Operating System

Leg Planner

Coordinates Cartesian planning and trajectory mapping.
"""

from titan.motion.foot_planner import FootPlanner
from titan.motion.trajectory import LegTrajectory
from titan.motion.trajectory_mapper import TrajectoryMapper
from titan.motion.foot_pose import FootPose


class LegPlanner:
    """
    Generates executable leg trajectories by composing
    a FootPlanner and a TrajectoryMapper.
    """

    def __init__(
        self,
        foot_planner: FootPlanner,
        mapper: TrajectoryMapper,
    ):
        self.foot_planner = foot_planner
        self.mapper = mapper

    def generate(
        self,
        foot_start: FootPose,
        foot_end: FootPose,
        duration: float = 1.0,
        dt: float = 0.02,
    ) -> LegTrajectory:
        """
        Generate an executable leg trajectory.
        """

        foot_trajectory = self.foot_planner.generate(
            start=foot_start,
            end=foot_end,
            duration=duration,
            dt=dt,
        )

        return self.mapper.map(
            foot_trajectory,
        )