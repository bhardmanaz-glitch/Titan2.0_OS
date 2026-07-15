"""
Titan 2.0 Operating System

Engineering Experiment
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class EngineeringExperiment:
    """
    Metadata describing an engineering experiment.
    """

    identifier: str

    description: str