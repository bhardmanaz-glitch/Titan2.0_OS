"""
Titan2_OS

Trajectory Executor

Executes a generated Trajectory using an AxisDriver.
"""

import time

from titan.hardware.axis_driver import AxisDriver
from collections.abc import Callable
from titan.motion.trajectory import (
    MotionPoint,
    Trajectory,
)
from titan.hardware.commissioned_joint import (
    CommissionedJoint,
)

class TrajectoryExecutor:

    def __init__(
        self,
        joint: CommissionedJoint,
        *,
        delay=0.0,
        callback=None,
    ):

        self.joint = joint

        self.delay = delay

        self.callback = callback

        self._running = False

        self._stop_requested = False

    def execute(
        self,
        trajectory: Trajectory,
        *,
        on_motion_point: Callable[[MotionPoint], None] | None = None,
    ) -> Trajectory:

        self._running = True
        self._stop_requested = False

        try:

            for point in trajectory:

                if self._stop_requested:
                    break

                start_time = time.perf_counter()

                self.process_point(point)

                if self.delay:
                    time.sleep(self.delay)

                if on_motion_point is not None:
                    on_motion_point(point)

                self._wait_until_next_point(
                    start_time,
                    point.dt,
                )

        finally:

            self._running = False

        return trajectory

    def process_point(
        self,
        point: MotionPoint,
    ) -> None:
        """
        Execute a single MotionPoint.
        """

        command = self.joint.mapper.map(
            point.position,
        )

        self.joint.driver.move_to(
            command.position,
        )

        if self.callback:
            self.callback(point)

    def _wait_until_next_point(
        self,
        start_time: float,
        dt: float,
    ) -> None:
        """
        Wait until the next trajectory sample should execute.
        """

        elapsed = time.perf_counter() - start_time

        remaining = dt - elapsed

        if remaining > 0:
            time.sleep(remaining)

    @property
    def running(self) -> bool:
        """
        True while a trajectory is executing.
        """
        return self._running


    @property
    def stop_requested(self) -> bool:
        """
        True if execution has been asked to stop.
        """
        return self._stop_requested

    def stop(self) -> None:
        """
        Request execution to stop.

        The current MotionPoint will finish executing,
        then execution will terminate.
        """

        self._stop_requested = True