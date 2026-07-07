from titan.motion.trajectory import LegTrajectory


class LegPlanner:
    """
    Uses inverse kinematics to convert a foot movement into
    synchronized hip and knee trajectories.
    """

    def __init__(
        self,
        ik_solver,
        trajectory_planner,
    ):
        self.ik_solver = ik_solver
        self.trajectory_planner = trajectory_planner

    def generate(
    self,
    foot_start,
    foot_end,
    duration=None,
    dt=0.02,
    ):

        start = self.ik_solver.solve(*foot_start)
        end = self.ik_solver.solve(*foot_end)

        if not start.reachable:
            raise ValueError("Starting foot position is unreachable.")

        if not end.reachable:
            raise ValueError("Ending foot position is unreachable.")

        #
        # First determine how long each joint needs.
        #
        hip_plan = self.trajectory_planner.plan(
            start=start.hip,
            end=end.hip,
            duration=duration,
            dt=dt,
        )

        knee_plan = self.trajectory_planner.plan(
            start=start.knee,
            end=end.knee,
            duration=duration,
            dt=dt,
        )

        #
        # Synchronize the joints.
        #
        if duration is None:
            duration = max(
                hip_plan.duration,
                knee_plan.duration,
            )

        #
        # Now generate synchronized trajectories.
        #
        hip = self.trajectory_planner.generate(
            start=start.hip,
            end=end.hip,
            duration=duration,
            dt=dt,
        )

        knee = self.trajectory_planner.generate(
            start=start.knee,
            end=end.knee,
            duration=duration,
            dt=dt,
        )

        return LegTrajectory(
            hip=hip,
            knee=knee,
        )