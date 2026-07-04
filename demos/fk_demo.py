from titan.math.ik import solve_ik
from titan.math.fk import solve_fk

x = 0.0
y = -0.292

result = solve_ik(
    x=x,
    y=y,
    l1=0.160,
    l2=0.165,
)

fk = solve_fk(
    hip=result.hip,
    knee=result.knee,
    l1=0.160,
    l2=0.165,
)

print()

print("Original Position")
print("-----------------")
print(f"x = {x:.6f}")
print(f"y = {y:.6f}")

print()

print("IK Solution")
print("-----------")
print(f"Hip  = {result.hip:.6f} rad")
print(f"Knee = {result.knee:.6f} rad")

print()

print("FK Result")
print("---------")
print(f"x = {fk.x:.6f}")
print(f"y = {fk.y:.6f}")

print()

print("Position Error")
print("--------------")
print(f"dx = {fk.x - x:.12f}")
print(f"dy = {fk.y - y:.12f}")