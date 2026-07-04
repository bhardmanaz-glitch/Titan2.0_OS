"""
Titan 2.0 Operating System

Forward Kinematics
"""

from dataclasses import dataclass
import math

@dataclass
class FKResult:
    """
    Result of forward kinematics.
    """

    x: float
    y: float

def solve_fk(
    hip: float,
    knee: float,
    l1: float,
    l2: float,
) -> FKResult:
    """
    Compute foot position from joint angles.

    Parameters
    ----------
    hip
        Hip angle (rad)

    knee
        Knee angle (rad)

    l1
        Thigh length (m)

    l2
        Shin length (m)
    """

    knee_global = hip + knee

    x = (
        l1 * math.cos(hip)
        + l2 * math.cos(knee_global)
    )

    y = (
        l1 * math.sin(hip)
        + l2 * math.sin(knee_global)
    )

    return FKResult(
        x=x,
        y=y,
    )