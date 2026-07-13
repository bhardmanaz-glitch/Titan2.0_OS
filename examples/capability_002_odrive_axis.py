"""
Titan 2.0 Operating System

Capability 002

ODrive Axis Verification

Safely verify communication with one ODrive axis.
"""

import time

from titan.hardware.odrive_axis import ODriveAxis


def main():

    print()
    print("=" * 50)
    print(" Titan Capability 002")
    print(" ODrive Axis Verification")
    print("=" * 50)
    print()

    axis = ODriveAxis(
        serial_number="422860447003",
        axis_index=0,
    )

    print("Connecting...")
    axis.connect()

    print("Connected")
    print()

    print(f"Position     : {axis.position:.5f}")
    print(f"Velocity     : {axis.velocity:.5f}")
    print(f"Voltage      : {axis.bus_voltage:.2f}")
    print(f"Temperature  : {axis.temperature:.2f}")
    print()

    print("Entering Closed Loop...")
    axis.enter_closed_loop()

    time.sleep(0.5)

    print("Moving to 0.05 rev...")
    axis.move_to(0.05)

    time.sleep(2.0)

    axis.refresh()

    print(f"Position : {axis.position:.5f}")
    print()

    print("Returning Home...")
    axis.move_to(0.0)

    time.sleep(2.0)

    axis.refresh()

    print(f"Position : {axis.position:.5f}")
    print()

    print("Entering Idle...")
    axis.enter_idle()

    print("Disconnecting...")
    axis.disconnect()

    print()
    print("Capability 002 PASSED")
    print()


if __name__ == "__main__":
    main()