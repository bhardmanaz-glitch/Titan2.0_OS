"""
===========================================================
Titan2_OS
robot.py

Author:
    Brandon Hardman
    OpenAI Robotics Team

Purpose
-------
Defines Titan's hardware layout.

This module builds the robot using the data structures
defined in models.py.

No CAN communication occurs here.
No joystick code.
No inverse kinematics.

This file simply describes what Titan IS.
===========================================================
"""

from titan.models import (
    Motor,
    Encoder,
    Joint,
    Leg,
    RobotState,
)

from titan.hardware.odrive import ODriveAxis

class TitanRobot:
    """
    Titan 2.0 robot definition.
    """

    def __init__(self):

        ####################################################
        # LEFT HIP
        ####################################################

        left_hip_motor = OdriveAxis(
            name="Left Hip",
            axis_id=0
        )

        left_hip_encoder = Encoder()

        left_hip = Joint(
            name="Left Hip",
            motor=left_hip_motor,
            encoder=left_hip_encoder
        )

        ####################################################
        # LEFT KNEE
        ####################################################

        left_knee_motor = OdriveAxis(
            name="Left Knee",
            axis_id=1
        )

        left_knee_encoder = Encoder()

        left_knee = Joint(
            name="Left Knee",
            motor=left_knee_motor,
            encoder=left_knee_encoder
        )

        ####################################################
        # LEFT LEG
        ####################################################

        self.left_leg = Leg(
            name="Left Leg",
            hip=left_hip,
            knee=left_knee
        )

        ####################################################
        # RIGHT LEG
        ####################################################
        #
        # Placeholder for now.
        # Hardware will be added later.
        #
        ####################################################

        self.right_leg = None

        ####################################################
        # ROBOT STATE
        ####################################################

        self.state = RobotState(
            enabled=False,
            battery_voltage=0.0,
            legs=[self.left_leg]
        )

    ########################################################
    # Utility Functions
    ########################################################

    def enable(self):

        self.state.enabled = True

    def disable(self):

        self.state.enabled = False

    def print_summary(self):

        print("\n========== Titan 2.0 ==========")

        print(f"Enabled : {self.state.enabled}")

        print()

        print(self.left_leg.name)

        print(f"  Hip  : {self.left_leg.hip.motor.name}")

        print(f"  Knee : {self.left_leg.knee.motor.name}")

        print()

        print("===============================\n")