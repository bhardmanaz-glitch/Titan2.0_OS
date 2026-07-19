from titan.hardware.controller_driver import ControllerDriver
from titan.hardware.odrive_discovery import ODriveDiscovery

class ODriveUSBController(ControllerDriver):

    def __init__(
        self,
        serial_number: str,
        channel: int,
    ):

        #
        # Identity
        #

        self._serial_number = serial_number

        self._channel = channel

        #
        # Hardware
        #

        self._driver = None

        self._axis = None

        #
        # State
        #

        self._connected = False

        self._telemetry = None

        #
        # Discovery
        #

        self._discovery = ODriveDiscovery()

    def _require_connection(self):

        if not self._connected:

            raise RuntimeError(
                "Controller not connected."
            )

    def connect(self):

        if self.connected:
            return

        self._driver = self._discovery.find(
            self._serial_number
        )

        print(type(self._driver))
        print(dir(self._driver))

        if self._channel == 0:

            self._axis = self._driver.axis0

        elif self._channel == 1:

            self._axis = self._driver.axis1

        else:

            raise ValueError(
                f"Invalid channel {self._channel}"
            )

        self._connected = True


    def enter_closed_loop(self):
        self._require_connection()
        raise NotImplementedError

    def enter_idle(self):
        self._require_connection()
        raise NotImplementedError

    def set_velocity(
        self,
        velocity: float,
    ):
        self._require_connection()
        raise NotImplementedError

    def stop(self):
        self._require_connection()
        raise NotImplementedError

    def refresh(self):
        self._require_connection()
        raise NotImplementedError

    def move_to(
        self,
        position: float,
    ):

        self._require_connection()

        self._axis.controller.input_pos = position

    def disconnect(self):

        self._driver = None

        self._connected = False   

        self._axis = None

    @property
    def driver(self):
        return self._driver

    @property
    def connected(self):
        return self._connected

    @property
    def axis(self):
        return self._axis
    