"""
Titan 2.0 Operating System

Capability 003

Position Motion Verification
"""

import time

from titan.hardware.odrive_axis import ODriveAxis


def main():

    print()
    print("=" * 50)
    print("Titan Capability 003")
    print("Position Motion Verification")
    print("=" * 50)
    print()

    axis = ODriveAxis()

    print("Connecting...")
    axis.connect()

    try:

        print("Connected")
        print()

        print("Entering Closed Loop...")
        axis.enter_closed_loop()

        targets = [
            0.05,
            0.10,
            -0.05,
            0.00,
        ]

        for target in targets:

            print(f"Target : {target:.5f} rev")
            print(f"Actual : {axis.position:.5f} rev")
            print(f"Error  : {axis.position - target:+.5f} rev")
            print()

            axis.move_to(target)

            # Give the motor time to move
            time.sleep(1.0)

            # Read latest telemetry
            axis.refresh()

            print(f"Actual Position : {axis.position:.5f}")
            print()

    finally:

        print("Entering Idle...")
        axis.enter_idle()

        print("Disconnecting...")
        axis.disconnect()

    print()
    print("Capability 003 PASSED")
    print()


if __name__ == "__main__":
    main()