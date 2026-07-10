from dataclasses import dataclass


@dataclass(frozen=True)
class FootPose:
    """
    Cartesian foot position relative to the hip joint.
    """

    x: float
    y: float