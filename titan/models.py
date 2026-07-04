"""
===========================================================
Titan2_OS
models.py

Author:
    Brandon Hardman
    OpenAI Robotics Team

Purpose
-------
Defines the data structures used throughout Titan2_OS.

This module contains NO robot logic.

It does NOT:
    - talk to motors
    - perform inverse kinematics
    - send CAN messages
    - read controllers

It ONLY describes hardware and robot state.

Every other module in Titan2_OS imports these classes.
===========================================================
"""

from dataclasses import dataclass, field
from typing import List


# ===========================================================
# Motor
# ===========================================================

@dataclass
class Motor:
    """
    Represents a physical motor.

    All units are SI.
    """

    name: str

    axis_id: int

    position: float = 0.0      # radians

    velocity: float = 0.0      # rad/sec

    torque: float = 0.0        # Nm

    current: float = 0.0       # Amps

    temperature: float = 0.0   # Celsius

    enabled: bool = False


# ===========================================================
# Encoder
# ===========================================================

@dataclass
class Encoder:
    """
    Represents an encoder attached to a motor.
    """

    raw: float = 0.0

    position: float = 0.0

    velocity: float = 0.0

    offset: float = 0.0


# ===========================================================
# Joint
# ===========================================================

@dataclass
class Joint:
    """
    A robot joint.

    A joint consists of one motor and one encoder.
    """

    name: str

    motor: Motor

    encoder: Encoder

    angle: float = 0.0         # radians

    command: float = 0.0        # desired angle (rad)


# ===========================================================
# Foot Pose
# ===========================================================

@dataclass
class FootPose:
    """
    Cartesian foot position.

    Units:
        meters
    """

    x: float = 0.0

    y: float = 0.0


# ===========================================================
# Leg
# ===========================================================

@dataclass
class Leg:
    """
    Complete robot leg.
    """

    name: str

    hip: Joint

    knee: Joint

    foot: FootPose = field(default_factory=FootPose)


# ===========================================================
# Robot State
# ===========================================================

@dataclass
class RobotState:
    """
    Global robot state.

    More items will be added as Titan grows.
    """

    enabled: bool = False

    battery_voltage: float = 0.0

    legs: List[Leg] = field(default_factory=list)