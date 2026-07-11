from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class MotionPoint(Generic[T]):
    position: T
    velocity: float
    acceleration: float
    time: float
    dt: float

@dataclass
class MotionPlan:
    start: float
    end: float

    distance: float
    direction: int

    duration: float

    max_velocity: float
    max_acceleration: float

    accel_time: float
    cruise_time: float
    decel_time: float

    accel_distance: float
    cruise_distance: float
    decel_distance: float

    steps: int
    dt: float


@dataclass(frozen=True)
class Trajectory(Generic[T]):
    points: list[MotionPoint[T]]

    duration: float
    distance: float
    dt: float

    start: T
    end: T

    metadata: dict = field(default_factory=dict)

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return iter(self.points)

    def __getitem__(self, index):
        return self.points[index]

    @property
    def first(self):
        return self.points[0]

    @property
    def last(self):
        return self.points[-1]

    @property
    def sample_count(self):
        return len(self.points)
    
@dataclass
class LegTrajectory:
    hip: Trajectory
    knee: Trajectory

    @property
    def duration(self):
        return max(
            self.hip.duration,
            self.knee.duration,
        )

    @property
    def sample_count(self):
        return max(
            len(self.hip),
            len(self.knee),
        )
    
    def __iter__(self):
        yield self.hip
        yield self.knee


