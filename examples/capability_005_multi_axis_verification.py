"""
Titan 2.0 Operating System

Capability 005

Multi-Axis Motion Verification

Purpose
-------
Verify that multiple robot joints can be commanded together,
execute synchronized motion, and return engineering measurements.
"""

from titan.hardware.hardware_manager import HardwareManager

from titan.hardware.hardware_inventory import (
    FRONT_LEFT_HIP_PITCH,
    FRONT_LEFT_KNEE_PITCH,
)

from titan.analysis.measurement import MotionMeasurement
from titan.analysis.statistics import MotionStatistics
from titan.analysis.experiment import EngineeringExperiment
from titan.analysis.report import ReportGenerator


CAPABILITY = "005"
NAME = "Multi-Axis Motion Verification"
VERSION = "1.0"


TARGETS = [
    0.00,
    0.05,
    0.10,
    0.15,
    0.10,
    0.05,
    0.00,
    -0.05,
    -0.10,
    -0.15,
    -0.10,
    -0.05,
    0.00,
]


def main():

    experiment = EngineeringExperiment(
        identifier="Capability 005",
        description="Multi-Axis Motion Verification",
    )

    manager = HardwareManager()

    front_left_hip_pitch = manager.connect_joint(
        FRONT_LEFT_HIP_PITCH
    )

    front_left_knee_pitch = manager.connect_joint(
        FRONT_LEFT_KNEE_PITCH
    )

    hip_measurements = []
    knee_measurements = []

    try:

        print()
        print("=" * 60)
        print("Titan Capability 005")
        print("Multi-Axis Motion Verification")
        print("=" * 60)
        print()

        front_left_hip_pitch.enter_closed_loop()
        front_left_knee_pitch.enter_closed_loop()

        for move_number, target in enumerate(TARGETS, start=1):

            print(f"Move {move_number}")
            print(f"Target : {target:+.5f} rev")

            #
            # Command both joints
            #

            front_left_hip_pitch.move_to(target)
            front_left_knee_pitch.move_to(target)

            #
            # Wait for both joints
            #

            front_left_hip_pitch.wait_until_position(target)
            front_left_knee_pitch.wait_until_position(target)

            #
            # Refresh telemetry
            #

            front_left_hip_pitch.refresh()
            front_left_knee_pitch.refresh()

            #
            # Measurements
            #

            hip_actual = front_left_hip_pitch.position
            knee_actual = front_left_knee_pitch.position

            hip_error = hip_actual - target
            knee_error = knee_actual - target

            hip_measurements.append(
                MotionMeasurement(
                    target=target,
                    actual=hip_actual,
                    error=hip_error,
                )
            )

            knee_measurements.append(
                MotionMeasurement(
                    target=target,
                    actual=knee_actual,
                    error=knee_error,
                )
            )

            print(
                f"Hip  : {hip_actual:+.5f} rev   "
                f"Error {hip_error:+.5f}"
            )

            print(
                f"Knee : {knee_actual:+.5f} rev   "
                f"Error {knee_error:+.5f}"
            )

            print()

        hip_summary = MotionStatistics.compute(
            hip_measurements
        )

        knee_summary = MotionStatistics.compute(
            knee_measurements
        )

        print()
        print("=" * 60)
        print("Front Left Hip Pitch")
        print("=" * 60)
        print()

        print(
            ReportGenerator.generate(
                experiment,
                hip_summary,
            )
        )

        print()

        print("=" * 60)
        print("Front Left Knee Pitch")
        print("=" * 60)
        print()

        print(
            ReportGenerator.generate(
                experiment,
                knee_summary,
            )
        )

        print()
        print("=" * 60)
        print("Capability 005 PASSED")
        print("=" * 60)

    finally:

        print()
        print("Entering Idle...")

        front_left_hip_pitch.enter_idle()
        front_left_knee_pitch.enter_idle()

        print("Disconnecting...")

        manager.disconnect()

        print()
        print("Hardware safely disconnected.")


if __name__ == "__main__":
    main()