from titan.motion.planner import TrajectoryPlanner
from titan.motion.profiles import TrapezoidalProfile

planner = TrajectoryPlanner(
    profile=TrapezoidalProfile(),
)

trajectory = planner.generate(
    start=0.0,
    end=1.0,
    dt=0.1,
)

print(f"\nGenerated {len(trajectory)} points\n")

for point in trajectory:
    print(point)