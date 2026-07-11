from titan.motion.foot_pose import FootPose
from titan.motion.robot_trajectory import RobotTrajectory


class RobotTrajectoryPlanner:
    """
    Coordinates four LegPlanners to generate a synchronized robot trajectory.
    """

    def __init__(
        self,
        left_front,
        right_front,
        left_rear,
        right_rear,
    ):
        self.left_front = left_front
        self.right_front = right_front
        self.left_rear = left_rear
        self.right_rear = right_rear

    def generate(
        self,
        left_front_start,
        left_front_end,
        right_front_start,
        right_front_end,
        left_rear_start,
        left_rear_end,
        right_rear_start,
        right_rear_end,
        duration: float = 1.0,
        dt: float = 0.02,
    ):

        fl = self.left_front.generate(
            foot_start=FootPose(*left_front_start),
            foot_end=FootPose(*left_front_end),
            duration=duration,
            dt=dt,
        )

        fr = self.right_front.generate(
            foot_start=FootPose(*right_front_start),
            foot_end=FootPose(*right_front_end),
            duration=duration,
            dt=dt,
        )

        rl = self.left_rear.generate(
            foot_start=FootPose(*left_rear_start),
            foot_end=FootPose(*left_rear_end),
            duration=duration,
            dt=dt,
        )

        rr = self.right_rear.generate(
            foot_start=FootPose(*right_rear_start),
            foot_end=FootPose(*right_rear_end),
            duration=duration,
            dt=dt,
        )

        return RobotTrajectory(
            left_front=fl,
            right_front=fr,
            left_rear=rl,
            right_rear=rr,
        )
            