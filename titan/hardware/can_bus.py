import can


class CANBus:
    """
    Shared SocketCAN interface.

    Owns the Linux CAN socket used by every
    controller driver.
    """

    def __init__(
        self,
        channel: str = "can0",
        bitrate: int = 250000,
    ):

        self.channel = channel
        self.bitrate = bitrate

        self._bus = None

        self._connected = False

    # -----------------------------------------

    def connect(self):

        if self._connected:
            return

        self._bus = can.interface.Bus(
            channel=self.channel,
            interface="socketcan",
        )

        self._connected = True

    # -----------------------------------------

    def disconnect(self):

        if self._bus is not None:

            self._bus.shutdown()

        self._bus = None

        self._connected = False

    # -----------------------------------------

    def send(
        self,
        message,
    ):

        if not self.connected:

            raise RuntimeError(
                "CAN bus is not connected."
            )

        self._bus.send(message)

    # -----------------------------------------

    def receive(
        self,
        timeout=None,
    ):

        if not self.connected:

            raise RuntimeError(
                "CAN bus is not connected."
            )

        return self._bus.recv(timeout)

    # -----------------------------------------

    @property
    def connected(self):

        return self._connected