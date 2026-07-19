"""
Titan 2.0 Operating System

Hardware Inventory

Defines the physical hardware installed on Titan.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class JointHardware:
    """
    Describes how Titan communicates with a physical joint.

    This class intentionally contains no vendor-specific terminology.
    It identifies the controller assigned to a joint without assuming
    any particular motor controller implementation.
    """

    identifier: str
    name: str

    controller_type: str
    controller_address: int | str
    controller_channel: int

    can_id: int


# ============================================================
# Front Left Leg
# ============================================================

FRONT_LEFT_HIP_PITCH = JointHardware(
    identifier="FL_HIP_PITCH",
    name="Front Left Hip Pitch",

    controller_type="odrive",
    controller_address="422860447003",
    controller_channel=0,

    can_id=10,
)

FRONT_LEFT_KNEE_PITCH = JointHardware(
    identifier="FL_KNEE_PITCH",
    name="Front Left Knee Pitch",

    controller_type="odrive",
    controller_address="422860457007",
    controller_channel=0,

    can_id=11,
)