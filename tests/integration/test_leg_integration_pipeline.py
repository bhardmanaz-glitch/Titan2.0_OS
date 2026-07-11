import pytest

from titan.motion.executor import TrajectoryExecutor
from titan.motion.foot_pose import FootPose
from titan.hardware.mock_axis import MockAxis
from titan.motion.leg_executor import LegExecutor


def test_leg_pipeline_executes_motion(
    leg_planner,
):

    start = FootPose(
        x=0.10,
        y=-0.15,
    )

    end = FootPose(
        x=0.15,
        y=-0.15,
    )

    trajectory = leg_planner.generate(
        foot_start=start,
        foot_end=end,
        dt=0.02,
    )

    hip_axis = MockAxis()
    knee_axis = MockAxis()

    hip_executor = TrajectoryExecutor(
    driver=hip_axis,
    )

    knee_executor = TrajectoryExecutor(
    driver=knee_axis,
    )

    executor = LegExecutor(
        hip_executor=hip_executor,
        knee_executor=knee_executor,
    )

    executor.execute(
    trajectory,
)
    
    assert len(hip_axis.commanded_positions) > 0
    assert len(knee_axis.commanded_positions) > 0

    assert hip_axis.commanded_positions[-1] == trajectory.hip.last.position

    assert knee_axis.commanded_positions[-1] == trajectory.knee.last.position