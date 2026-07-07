from titan.motion.planner import TrajectoryPlanner

planner = TrajectoryPlanner()

trajectory = planner.generate(
    start=0.0,
    end=0.5,
    duration=0.5,
)

print()
print("Duration Controlled Trajectory")
print("-" * 50)

for point in trajectory:
    print(
        f"Pos={point.position:6.3f} "
        f"Vel={point.velocity:6.3f} "
        f"Time={point.time:5.2f}"
    )

print()
print(f"Generated {len(trajectory)} points")
print(f"Final Time = {trajectory[-1].time:.2f} seconds")
print(f"Final Position = {trajectory[-1].position:.3f}")
print(f"Velocity = {trajectory[0].velocity:.3f} rad/s")