from abc import ABC, abstractmethod
from titan.motion.trajectory import Trajectory
from typing import Generic, TypeVar

T = TypeVar("T")


class MotionBehavior(ABC, Generic[T]):

    @abstractmethod
    def generate(
        self,
        start: T,
        end: T,
        duration: float,
        dt: float,
    ) -> Trajectory[T]:
        ...