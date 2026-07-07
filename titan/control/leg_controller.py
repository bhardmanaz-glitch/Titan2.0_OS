import time

from titan.control.joint_controller import JointController


class LegController:

    def __init__(self, hip_joint, knee_joint):

        self.hip = JointController(hip_joint)
        self.knee = JointController(knee_joint)

    def follow(self, trajectory):

        hip_path = trajectory.hip
        knee_path = trajectory.knee

        if len(hip_path) != len(knee_path):
            raise ValueError("Hip and knee trajectories must be the same length.")

        self.hip.joint.enable()
        self.knee.joint.enable()

        start_time = time.perf_counter()

        try:

            for hip_point, knee_point in zip(hip_path, knee_path):

                target_time = start_time + hip_point.time

                remaining = target_time - time.perf_counter()

                if remaining > 0:
                    time.sleep(remaining)

                self.hip.command(hip_point)
                self.knee.command(knee_point)

                actual_time = time.perf_counter() - start_time

                print(
                    f"T={actual_time:5.2f} | "
                    f"Hip={hip_point.position:6.3f} | "
                    f"Knee={knee_point.position:6.3f}"
                )

            total_time = time.perf_counter() - start_time

            print()
            print(f"Trajectory complete in {total_time:.3f} seconds")
            print(f"Expected duration      {hip_path[-1].time:.3f} seconds")
            print(f"Timing error           {(total_time - hip_path[-1].time) * 1000:.2f} ms")

        finally:

            self.hip.joint.disable()
            self.knee.joint.disable()