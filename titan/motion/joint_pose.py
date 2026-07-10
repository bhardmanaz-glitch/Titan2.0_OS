"""
Titan 2.0 Operating System

Joint Pose

Represents a desired pose for a single leg in joint space.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class JointPose:
    """
    Desired joint-space pose.

    Angles are expressed in degrees.
    """

    hip: float
    knee: float