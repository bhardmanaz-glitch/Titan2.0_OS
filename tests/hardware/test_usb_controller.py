#!/usr/bin/env python3
"""
Titan 2.0 OS
USB Controller Verification Test

Verifies:

    ✓ Construction
    ✓ Connect
    ✓ Disconnect
    ✓ Reconnect
    ✓ Axis 0 binding
    ✓ Axis 1 binding

This test intentionally does NOT:

    - Enter closed loop
    - Command motion
    - Read telemetry
"""

from titan.hardware.odrive_usb_controller import ODriveUSBController


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

SERIAL_NUMBER = "006274725D1B"


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def banner(title: str):

    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


def check(description: str, condition: bool):

    if condition:
        print(f"[PASS] {description}")
    else:
        raise AssertionError(f"[FAIL] {description}")


# ---------------------------------------------------------------------
# Lifecycle Test
# ---------------------------------------------------------------------

def test_channel(channel: int):

    banner(f"Testing Channel {channel}")

    controller = ODriveUSBController(
        serial_number=SERIAL_NUMBER,
        channel=channel,
    )

    check(
        "Controller starts disconnected",
        controller.connected is False,
    )

    controller.connect()

    check(
        "Controller connected",
        controller.connected,
    )

    check(
        "Driver object created",
        controller.driver is not None,
    )

    check(
        "Axis object bound",
        controller.axis is not None,
    )

    expected_axis = (
        controller.driver.axis0
        if channel == 0
        else controller.driver.axis1
    )

    check(
        f"Bound to axis{channel}",
        controller.axis is expected_axis,
    )

    controller.disconnect()

    check(
        "Controller disconnected",
        controller.connected is False,
    )

    check(
        "Axis released",
        controller.axis is None,
    )

    check(
        "Driver released",
        controller.driver is None,
    )


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():

    banner("USB Controller Lifecycle Test")

    #
    # Test axis 0
    #

    test_channel(0)

    #
    # Test reconnect
    #

    banner("Reconnect Test")

    controller = ODriveUSBController(
        serial_number=SERIAL_NUMBER,
        channel=0,
    )

    controller.connect()

    check(
        "Initial connection",
        controller.connected,
    )

    controller.disconnect()

    check(
        "Disconnected",
        controller.connected is False,
    )

    controller.connect()

    check(
        "Reconnect successful",
        controller.connected,
    )

    controller.disconnect()

    check(
        "Final disconnect",
        controller.connected is False,
    )

    #
    # Test axis 1
    #

    test_channel(1)

    banner("USB Controller Test PASSED")


if __name__ == "__main__":

    try:

        main()

    except Exception as ex:

        banner("TEST FAILED")

        print(type(ex).__name__)
        print(ex)

        raise