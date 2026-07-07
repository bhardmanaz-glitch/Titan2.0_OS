from abc import ABC, abstractmethod


class MotionProfile(ABC):
    """
    Base class for all motion profiles.
    """

    @abstractmethod
    def generate(self, plan):
        """
        Generate a trajectory from a MotionPlan.
        """
        pass