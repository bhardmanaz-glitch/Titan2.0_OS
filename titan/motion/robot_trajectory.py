from dataclasses import dataclass

from titan.motion.trajectory import LegTrajectory


@dataclass
class RobotTrajectory:
    front_left: LegTrajectory
    front_right: LegTrajectory
    rear_left: LegTrajectory
    rear_right: LegTrajectory
    

    @property
    def legs(self):
        return (
            self.front_left,
            self.front_right,
            self.rear_left,
            self.rear_right,
        )

    @property
    def duration(self):
        return max(leg.duration for leg in self.legs)

    @property
    def sample_count(self):
        return max(leg.sample_count for leg in self.legs)
    
    def __iter__(self):
        return iter(self.legs)

    def __len__(self):
        return len(self.legs)

    def __getitem__(self, index):
        return self.legs[index]
    
    def as_dict(self):
        return {
            "front_left": self.front_left,
            "front_right": self.front_right,
            "rear_left": self.rear_left,
            "rear_right": self.rear_right,
    }