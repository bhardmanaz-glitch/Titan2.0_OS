from titan.motion.scheduler import ExecutionScheduler
from titan.motion.executor import TrajectoryExecutor
from titan.motion.trajectory import LegTrajectory


class LegExecutor:
    """
    Executes synchronized hip and knee trajectories.
    """

    def __init__(
        self,
        hip_executor: TrajectoryExecutor,
        knee_executor: TrajectoryExecutor,
    ):
        self.hip_executor = hip_executor
        self.knee_executor = knee_executor

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
    
    class LegExecutor:

        def __init__(
            self,
            hip_executor,
            knee_executor,
        ):

            self.hip_executor = hip_executor
            self.knee_executor = knee_executor

            self.scheduler = ExecutionScheduler()