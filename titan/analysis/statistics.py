"""
Titan 2.0 Operating System

Motion Statistics
"""

import math

from titan.analysis.measurement import MotionMeasurement
from titan.analysis.summary import MotionStatisticsSummary


class MotionStatistics:
    """
    Computes statistics for a motion characterization experiment.
    """

    @staticmethod
    def compute(
        measurements: list[MotionMeasurement],
    ) -> MotionStatisticsSummary:

        if not measurements:
            raise ValueError(
                "No measurements supplied."
            )

        errors = [
            m.error
            for m in measurements
        ]

        abs_errors = [
            abs(e)
            for e in errors
        ]

        mean_error = (
            sum(errors)
            / len(errors)
        )

        mean_absolute_error = (
            sum(abs_errors)
            / len(abs_errors)
        )

        maximum_error = max(abs_errors)

        rms_error = math.sqrt(

            sum(
                e * e
                for e in errors
            )

            / len(errors)
        )

        standard_deviation = math.sqrt(

            sum(
                (e - mean_error) ** 2
                for e in errors
            )

            / len(errors)
        )

        return MotionStatisticsSummary(

            moves_tested=len(measurements),

            mean_error=mean_error,

            mean_absolute_error=mean_absolute_error,

            maximum_error=maximum_error,

            rms_error=rms_error,

            standard_deviation=standard_deviation,

            return_to_zero_error=measurements[-1].error,
        )