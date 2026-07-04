"""
Titan 2.0 Operating System

Inverse Kinematics
"""

from dataclasses import dataclass
import math

@dataclass
class IKResult:
    """
    Result of an inverse kinematics solve.
    """

    hip: float
    knee: float

    reachable: bool

def solve_ik(
    x: float,
    y: float,
    l1: float,
    l2: float,
    knee_forward: bool = True,
) -> IKResult:
    """
    Solve planar two-link inverse kinematics.

    Parameters
    ----------
    x, y
        Desired foot position (meters)

    l1
        Thigh length

    l2
        Shin length

    knee_forward
        True selects the normal walking solution.
    """

    r2 = x * x + y * y
    r = math.sqrt(r2)

    if r > (l1 + l2):
        return IKResult(
            hip=0.0,
            knee=0.0,
            reachable=False,
        )
    
    c = (
        r2
        - l1 * l1
        - l2 * l2
    ) / (2.0 * l1 * l2)

    c = max(min(c, 1.0), -1.0)

    if knee_forward:
        knee = -math.acos(c)
    else:
        knee = math.acos(c)

    k1 = l1 + l2 * math.cos(knee)
    k2 = l2 * math.sin(knee)

    hip = (
        math.atan2(y, x)
        - math.atan2(k2, k1)
    )

    return IKResult(
        hip=hip,
        knee=knee,
        reachable=True,
    )
        
