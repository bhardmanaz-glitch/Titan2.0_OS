"""
Titan 2.0 OS

Execution Scheduler

Coordinates synchronized iteration over one or more execution streams.
"""

from itertools import zip_longest


class ExecutionScheduler:
    """
    Synchronizes one or more execution streams.

    The scheduler is agnostic to the type of objects being scheduled.
    """

    def schedule(self, *streams):

        yield from zip_longest(*streams)