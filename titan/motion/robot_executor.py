from titan.motion.leg_executor import LegExecutor
from titan.motion.robot_trajectory import RobotTrajectory


class RobotExecutor:
    """
    Executes synchronized trajectories for an entire robot.
    """

    def __init__(
        self,
        left_front: LegExecutor,
        right_front: LegExecutor,
        left_rear: LegExecutor,
        right_rear: LegExecutor,
    ):

        self.left_front = left_front
        self.right_front = right_front
        self.left_rear = left_rear
        self.right_rear = right_rear

    def execute(
        self,
        trajectory: RobotTrajectory,
    ) -> RobotTrajectory:

        if trajectory is None:
            raise TypeError("trajectory cannot be None")

        if not isinstance(trajectory, RobotTrajectory):
            raise TypeError(
                f"Expected RobotTrajectory, got {type(trajectory).__name__}"
            )
        
    
        self.left_front.execute(
            trajectory.left_front,
        )

        self.right_front.execute(
            trajectory.right_front,
        )

        self.left_rear.execute(
            trajectory.left_rear,
        )

        self.right_rear.execute(
            trajectory.right_rear,
        )

        return trajectory