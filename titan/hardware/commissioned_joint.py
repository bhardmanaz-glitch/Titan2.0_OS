"""
Titan 2.0 Operating System

Runtime Hardware

Commissioned Joint
"""

from dataclasses import dataclass

from titan.hardware.axis_driver import AxisDriver
from titan.hardware.actuator_mapper import ActuatorMapper
from titan.hardware.joint import Joint


@dataclass(slots=True)
class CommissionedJoint:
    """
    Runtime representation of a physical joint.

    Couples the immutable Digital Twin Joint
    with the hardware used to control it.
    """

    joint: Joint

    driver: AxisDriver

    mapper: ActuatorMapper