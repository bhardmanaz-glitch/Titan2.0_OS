from titan.motion.robot_trajectory import RobotTrajectory


class RobotTrajectoryPlanner:
    """
    Coordinates four LegPlanners to generate a synchronized robot trajectory.
    """

    def __init__(
        self,
        front_left,
        front_right,
        rear_left,
        rear_right,
    ):
        self.front_left = front_left
        self.front_right = front_right
        self.rear_left = rear_left
        self.rear_right = rear_right

    def generate(
        self,
        front_left_start,
        front_left_end,
        front_right_start,
        front_right_end,
        rear_left_start,
        rear_left_end,
        rear_right_start,
        rear_right_end,
        duration=None,
        dt=0.02,
    ):

        fl = self.front_left.generate(
            foot_start=front_left_start,
            foot_end=front_left_end,
            duration=duration,
            dt=dt,
        )

        fr = self.front_right.generate(
            foot_start=front_right_start,
            foot_end=front_right_end,
            duration=duration,
            dt=dt,
        )

        rl = self.rear_left.generate(
            foot_start=rear_left_start,
            foot_end=rear_left_end,
            duration=duration,
            dt=dt,
        )

        rr = self.rear_right.generate(
            foot_start=rear_right_start,
            foot_end=rear_right_end,
            duration=duration,
            dt=dt,
        )

        return RobotTrajectory(
            front_left=fl,
            front_right=fr,
            rear_left=rl,
            rear_right=rr,
        )