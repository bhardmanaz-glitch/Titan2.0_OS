from titan.motion.planner import TrajectoryPlanner

planner = TrajectoryPlanner()

plan = planner.plan(
    start=0.0,
    end=0.9,
    duration=2.0,
)

print()
print("Motion Plan")
print("-" * 40)

print(f"Start      : {plan.start}")
print(f"End        : {plan.end}")
print(f"Distance   : {plan.distance}")
print(f"Direction  : {plan.direction}")
print(f"Duration   : {plan.duration:.3f}")
print(f"Max Velocity   : {plan.max_velocity:.3f}")
print(f"Max Accel      : {plan.max_acceleration:.3f}")

print()
print("Timing")
print("-" * 40)

print(f"Accel Time   : {plan.accel_time:.3f}")
print(f"Cruise Time  : {plan.cruise_time:.3f}")
print(f"Decel Time   : {plan.decel_time:.3f}")

print()
print("Distances")
print("-" * 40)

print(f"Accel Dist   : {plan.accel_distance:.3f}")
print(f"Cruise Dist  : {plan.cruise_distance:.3f}")
print(f"Decel Dist   : {plan.decel_distance:.3f}")

print()
print(f"Steps        : {plan.steps}")
print(f"dt           : {plan.dt}")