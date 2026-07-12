import pytest

from titan.hardware.commissioned_joint import CommissionedJoint
from titan.hardware.actuator_mapper import ActuatorMapper
from titan.hardware.prototype import PROTOTYPE_LEG
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

    hip_mapper = ActuatorMapper(
        gear_ratio=PROTOTYPE_LEG.hip.actuator.ratio,
        sign=1,
        zero_offset=0.0,
    )

    knee_mapper = ActuatorMapper(
        gear_ratio=PROTOTYPE_LEG.knee.actuator.ratio,
        sign=1,
        zero_offset=0.0,
    )

    hip_joint = CommissionedJoint(
        joint=PROTOTYPE_LEG.hip,
        driver=hip_axis,
        mapper=hip_mapper,
    )

    knee_joint = CommissionedJoint(
        joint=PROTOTYPE_LEG.knee,
        driver=knee_axis,
        mapper=knee_mapper,
    )

    executor = LegExecutor(
        hip_joint=hip_joint,
        knee_joint=knee_joint,
    )   

    executor.execute(
    trajectory,
)
    
    assert len(hip_axis.commanded_positions) > 0
    assert len(knee_axis.commanded_positions) > 0

    expected_hip = hip_joint.mapper.map(
        trajectory.hip.last.position
    )

    assert hip_axis.commanded_positions[-1] == pytest.approx(
        expected_hip.position
    )

    expected_knee = knee_joint.mapper.map(
        trajectory.knee.last.position
    )

    assert knee_axis.commanded_positions[-1] == pytest.approx(
        expected_knee.position
    )