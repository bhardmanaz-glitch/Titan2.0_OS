from titan.motion.behaviors import MotionBehavior
from titan.motion.foot_pose import FootPose

class FootPlanner:

    def __init__(
        self,
        behavior: MotionBehavior[FootPose],
    ):
        self.behavior = behavior

    def generate(
        self,
        start: FootPose,
        end: FootPose,
        duration: float,
        dt: float,
    ):
        return self.behavior.generate(
            start,
            end,
            duration,
            dt,
        )