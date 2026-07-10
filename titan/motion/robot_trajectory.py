from dataclasses import dataclass

from titan.motion.trajectory import LegTrajectory


@dataclass
class RobotTrajectory:
    left_front: LegTrajectory
    right_front: LegTrajectory
    left_rear: LegTrajectory
    right_rear: LegTrajectory
    

    @property
    def legs(self):
        return (
            self.left_front,
            self.right_front,
            self.left_rear,
            self.right_rear,
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
            "left_front": self.left_front,
            "right_front": self.right_front,
            "left_rear": self.left_rear,
            "right_rear": self.right_rear,
        }