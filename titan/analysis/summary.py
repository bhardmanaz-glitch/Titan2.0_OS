"""
Titan 2.0 Operating System

Motion Statistics Summary
"""

from dataclasses import dataclass
from titan.analysis.experiment import EngineeringExperiment


@dataclass(frozen=True)
class MotionStatisticsSummary:
    """
    Statistical summary of an engineering experiment.
    """

    moves_tested: int

    mean_error: float

    mean_absolute_error: float

    maximum_error: float

    rms_error: float

    standard_deviation: float

    return_to_zero_error: float

    def report(
        self,
        experiment: EngineeringExperiment,
        status: str = "PASSED",
    ) -> str:
        """
        Generate a reusable engineering report.
        """

        return "\n".join([

            "=" * 60,

            "Titan Engineering Report",

            "=" * 60,

            "",

            experiment.identifier,

            experiment.description,

            "",

            "-" * 60,

            "Statistical Summary",

            "-" * 60,

            "",

            f"Moves Tested         : {self.moves_tested}",

            "",

            f"Mean Error           : {self.mean_error:+.6f} rev",

            f"Mean Absolute Error  : {self.mean_absolute_error:.6f} rev",

            f"Maximum Error        : {self.maximum_error:.6f} rev",

            f"RMS Error            : {self.rms_error:.6f} rev",

            f"Standard Deviation   : {self.standard_deviation:.6f} rev",

            f"Return-To-Zero Error : {self.return_to_zero_error:+.6f} rev",

            "",

            "=" * 60,

            f"{experiment.identifier} {status}",

            "=" * 60,

        ])