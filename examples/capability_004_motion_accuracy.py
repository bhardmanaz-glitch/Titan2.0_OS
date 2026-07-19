"""
Titan 2.0 Operating System

Capability 004

Motion Accuracy Characterization

Measure actuator positioning accuracy and repeatability.
"""

import time

from titan.analysis.report import ReportGenerator
from titan.analysis.experiment import EngineeringExperiment
from titan.analysis.measurement import MotionMeasurement
from titan.analysis.statistics import MotionStatistics

from titan.hardware.odrive_axis import ODriveAxis


CAPABILITY = "004"
NAME = "Motion Accuracy Characterization"
VERSION = "1.0"


TARGETS = [
    0.00,
    0.05,
    0.10,
    0.15,
    0.20,
    0.15,
    0.10,
    0.05,
    0.00,
    -0.05,
    -0.10,
    -0.15,
    -0.20,
    -0.15,
    -0.10,
    -0.05,
    0.00,
]


def main():

    experiment = EngineeringExperiment(
        identifier="Capability 004",
        description="Motion Accuracy Characterization",
    )

    axis = ODriveAxis(
        serial_number="422860447003",
        axis_index=0,
    )

    measurements: list[MotionMeasurement] = []

    print()
    print("=" * 60)
    print(experiment.identifier)
    print(experiment.description)
    print("=" * 60)
    print()

    print("Connecting...")
    axis.connect()

    try:

        print("Connected")
        print()

        print("Entering Closed Loop...")
        axis.enter_closed_loop()
        print()

        for move_number, target in enumerate(TARGETS, start=1):

            print(f"Move {move_number:02d}")

            axis.move_to(target)

            #
            # Allow the actuator to settle.
            # Capability 004 is measuring behavior,
            # not evaluating controller tuning.
            #
            time.sleep(1.0)

            axis.refresh()

            actual = axis.position

            error = actual - target

            measurement = MotionMeasurement(
                target=target,
                actual=actual,
                error=error,
            )

            measurements.append(measurement)

            print(f"Target : {target:+8.5f} rev")
            print(f"Actual : {actual:+8.5f} rev")
            print(f"Error  : {error:+8.5f} rev")
            print()

        summary = MotionStatistics.compute(
            measurements
        )

        print(summary.report(experiment))

    finally:

        print()
        print("Entering Idle...")
        axis.enter_idle()

        print("Disconnecting...")
        axis.disconnect()

        print()
        print("Hardware safely disconnected.")


if __name__ == "__main__":
    main()