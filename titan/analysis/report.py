"""
Titan 2.0 Operating System

Engineering Report Generator
"""

from titan.analysis.experiment import EngineeringExperiment
from titan.analysis.summary import MotionStatisticsSummary


class ReportGenerator:
    """
    Generates standardized engineering reports for Titan
    capability verification.
    """

    @staticmethod
    def generate(
        experiment: EngineeringExperiment,
        summary: MotionStatisticsSummary,
    ) -> str:

        return f"""
============================================================
Titan Engineering Report
============================================================

{experiment.identifier}
{experiment.description}

------------------------------------------------------------
Statistical Summary
------------------------------------------------------------

Moves Tested        : {summary.moves_tested}

Mean Error          : {summary.mean_error:+.6f} rev
Mean Absolute Error : {summary.mean_absolute_error:.6f} rev
Maximum Error       : {summary.maximum_error:.6f} rev
RMS Error           : {summary.rms_error:.6f} rev
Standard Deviation  : {summary.standard_deviation:.6f} rev
Return-To-Zero      : {summary.return_to_zero_error:+.6f} rev
""".strip()