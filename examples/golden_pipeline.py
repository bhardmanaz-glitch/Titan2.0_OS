"""
Titan 2.0 Operating System

Capability 001

Golden Pipeline

Assemble the complete software pipeline using MockAxis.
No hardware is required.
"""


from titan.hardware.actuator_mapper import ActuatorMapper
from titan.hardware.commissioned_joint import CommissionedJoint
from titan.hardware.mock_axis import MockAxis
from titan.hardware.prototype import PROTOTYPE_LEG

from titan.motion.behaviors.trapezoidal_behavior import TrapezoidalBehavior
from titan.kinematics.inverse_kinematics import InverseKinematics
from titan.motion.foot_planner import FootPlanner
from titan.motion.trajectory_mapper import TrajectoryMapper
from titan.motion.foot_pose import FootPose
from titan.motion.leg_executor import LegExecutor
from titan.motion.leg_planner import LegPlanner

def build_pipeline():
    """
    Assemble the complete software pipeline.

    Returns
    -------
    tuple
        (planner, executor)
    """

    hip_joint = CommissionedJoint(
        joint=PROTOTYPE_LEG.hip,
        driver=MockAxis(),
        mapper=ActuatorMapper(
            gear_ratio=36,
            sign=1,
            zero_offset=0.0,
        ),
    )
    
    knee_joint = CommissionedJoint(
        joint=PROTOTYPE_LEG.knee,
        driver=MockAxis(),
        mapper=ActuatorMapper(
            gear_ratio=9,
            sign=1,
            zero_offset=0.0,
        ),
    )

    behavior = TrapezoidalBehavior()

    foot_planner = FootPlanner(
        behavior,
    )

    ik = InverseKinematics(
        PROTOTYPE_LEG,
    )

    trajectory_mapper = TrajectoryMapper(
        ik,
    )

    planner = LegPlanner(
        foot_planner=foot_planner,
        mapper=trajectory_mapper,
    )

    executor = LegExecutor(
        hip_joint=hip_joint,
        knee_joint=knee_joint,
    )

    return (
        planner, 
        executor,
    )

def main():
    """
    Capability 001.

    Assemble Titan's complete motion pipeline.
    """
    planner, executor = build_pipeline()

    start = FootPose(
        x=0.10,
        y=-0.15,
    )

    end = FootPose(
        x=0.15,
        y=-0.15,
    )

    trajectory = planner.generate(
        foot_start=start,
        foot_end=end,
        duration=1.0,
        dt=0.02,
    )

    executor.execute(trajectory)

    executor.hip_joint.driver.position
    executor.knee_joint.driver.position

    print()
    print(f"Hip points generated : {len(trajectory.hip)}")
    print(f"Knee points generated: {len(trajectory.knee)}")

    print()
    print("Final Driver Positions")
    print(f"Hip : {executor.hip_joint.driver.position:.4f}")
    print(f"Knee: {executor.knee_joint.driver.position:.4f}")

    print()
    print("Final Driver Positions")

    print(
        "Hip :",
        executor.hip_joint.driver.position,
    )

    print(
        "Knee:",
        executor.knee_joint.driver.position,
    )

    print()

    print("=" * 50)
    print(" Titan Golden Pipeline")
    print("=" * 50)

    print()

    print("Planner.............OK")
    print("Executor............OK")

    print()

    print("Pipeline assembled successfully.")

if __name__ == "__main__":
    main()