from abc import ABC, abstractmethod

from titan.motion.trajectory import Trajectory


class MotionBehavior(ABC):
    """
    Base class for generating joint motion trajectories.
    """

    @abstractmethod
    def generate(
        self,
        start: float,
        end: float,
    ) -> Trajectory:
        """
        Generate a trajectory between two joint positions.
        """
        ...