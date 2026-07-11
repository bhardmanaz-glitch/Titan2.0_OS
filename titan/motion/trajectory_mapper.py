"""
Titan 2.0 Operating System

Trajectory Mapper

Converts Cartesian foot trajectories into synchronized joint trajectories.
"""
from titan.motion.trajectory import MotionPoint
from titan.kinematics.inverse_kinematics import InverseKinematics
from titan.motion.foot_pose import FootPose
from titan.motion.trajectory import LegTrajectory
from titan.motion.trajectory import Trajectory


class TrajectoryMapper:
    """
    Maps a Cartesian foot trajectory into synchronized joint trajectories.

    This class owns the transformation between Cartesian space and
    joint space. It performs no planning and no hardware execution.
    """

    def __init__(
        self,
        inverse_kinematics: InverseKinematics,
    ):
        self.inverse_kinematics = inverse_kinematics

    def map(
        self,
        trajectory: Trajectory[FootPose],
    ) -> LegTrajectory:
        """
        Convert a Cartesian trajectory into a synchronized joint trajectory.
        """

        hip_points = []
        knee_points = []

        for point in trajectory.points:

            joint_pose = self.inverse_kinematics.solve(
                point.position,
            )

            hip_points.append(
                MotionPoint(
                    position=joint_pose.hip,
                    velocity=point.velocity,
                    acceleration=point.acceleration,
                    time=point.time,
                    dt=point.dt,
                )
            )

            knee_points.append(
                MotionPoint(
                    position=joint_pose.knee,
                    velocity=point.velocity,
                    acceleration=point.acceleration,
                    time=point.time,
                    dt=point.dt,
                )
            )

        hip = Trajectory(
            points=tuple(hip_points),
            duration=trajectory.duration,
            distance=trajectory.distance,
            dt=trajectory.dt,
            start=hip_points[0].position,
            end=hip_points[-1].position,
            metadata=trajectory.metadata,
        )

        knee = Trajectory(
            points=tuple(knee_points),
            duration=trajectory.duration,
            distance=trajectory.distance,
            dt=trajectory.dt,
            start=knee_points[0].position,
            end=knee_points[-1].position,
            metadata=trajectory.metadata,
        )   

        return LegTrajectory(
            hip=hip,
            knee=knee,
        )
    
    
    
    