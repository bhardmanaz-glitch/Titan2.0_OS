from dataclasses import dataclass, field


@dataclass
class MotionPoint:
    """
    One point in a trajectory.
    """

    position: float
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


@dataclass(slots=True)
class Trajectory:
    """
    A generated motion trajectory.

    Stores the generated MotionPoints together with
    the metadata used to generate them.
    """

    points: list[MotionPoint]

    duration: float
    distance: float

    dt: float

    start: float
    end: float

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


