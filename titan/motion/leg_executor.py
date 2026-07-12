from titan.hardware.commissioned_joint import CommissionedJoint
from titan.motion.scheduler import ExecutionScheduler
from titan.motion.executor import TrajectoryExecutor
from titan.motion.trajectory import LegTrajectory


class LegExecutor:
    """
    Executes synchronized hip and knee trajectories.
    """

    def __init__(
        self,
        hip_joint: CommissionedJoint,
        knee_joint: CommissionedJoint,
    ):
        self.hip_joint = hip_joint
        self.knee_joint = knee_joint

        self.hip_executor = TrajectoryExecutor(
            hip_joint,
        )

        self.knee_executor = TrajectoryExecutor(
            knee_joint,
        )

        self.scheduler = ExecutionScheduler()

    def execute(
        self,
        trajectory: LegTrajectory,
    ) -> LegTrajectory:
        """
        Execute hip and knee trajectories in lockstep.
        """

        for hip_point, knee_point in self.scheduler.schedule(
            trajectory.hip,
            trajectory.knee,
        ):

            if hip_point is not None:
                self.hip_executor.process_point(
                    hip_point,
                )

            if knee_point is not None:
                self.knee_executor.process_point(
                    knee_point,
                )

        return trajectory
    
    