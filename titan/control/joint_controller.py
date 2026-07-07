from titan.hardware.joint import Joint
import time


class JointController:

    def __init__(self, joint):
        self.joint = joint

    def command(self, point):
        self.joint.move_safe(point.position)

    def follow(self, trajectory):

        self.joint.enable()

        start_time = time.perf_counter()

        try:

            for point in trajectory:

                target_time = start_time + point.time

                remaining = target_time - time.perf_counter()

                if remaining > 0:
                    time.sleep(remaining)

                self.joint.move_safe(point.position)

                actual_time = time.perf_counter() - start_time

                error_ms = (actual_time - point.time) * 1000

                print(
                    f"{self.joint.name:8}"
                    f" Pos={point.position:6.3f}"
                    f" Vel={point.velocity:6.3f}"
                    f" Plan={point.time:5.2f}"
                    f" Actual={actual_time:5.2f}"
                    f" Error={error_ms:6.2f} ms"
                )

            total_time = time.perf_counter() - start_time

            print()
            print(f"Trajectory complete in {total_time:.3f} seconds")
            print(f"Expected duration      {trajectory[-1].time:.3f} seconds")
            print(f"Timing error           {(total_time - trajectory[-1].time)*1000:.2f} ms")

        finally:

            self.joint.disable()