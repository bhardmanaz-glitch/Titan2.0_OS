from titan.kinematics.ik import solve_ik

result = solve_ik(
    x=0.0,
    y=-0.292,
    l1=0.160,
    l2=0.165,
)

print(result)