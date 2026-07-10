"""
Titan2_OS

Mock Axis Driver

Software implementation of an AxisDriver.

Used for unit testing and planner development without physical hardware.
"""

from dataclasses import dataclass, field

from titan.hardware.axis_driver import AxisDriver
from titan.hardware.telemetry import Telemetry



@dataclass
class MockAxis(AxisDriver):
    """
    Software implementation of an axis driver.

    Behaves like a real motor controller but stores all state in memory.
    """

    _connected: bool = False

    _position: float = 0.0
    _velocity: float = 0.0
    _current: float = 0.0

    _bus_voltage: float = 24.0
    _bus_current: float = 0.0

    _temperature: float = 25.0

    _axis_state: str = "IDLE"

    _serial_number: str = "MOCK"
    _firmware_version: str = "0.0"

    _active_errors: list = field(default_factory=list)

    _disarm_reason: str | None = None

    _commanded_positions: list[float] = field(
        default_factory=list
    )

    _commanded_velocities: list[float] = field(
        default_factory=list
    )

    # ---------------------------------------------------------
    # Connection
    # ---------------------------------------------------------

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def refresh(self) -> Telemetry:
        """
        Return an immutable snapshot of the current axis state.
            """

        return Telemetry(
            position=self._position,
            velocity=self._velocity,
            current=self._current,
            temperature=self._temperature,
            bus_voltage=self._bus_voltage,
            bus_current=self._bus_current,
            axis_state=self._axis_state,
            active_errors=tuple(self._active_errors or ()),
            disarm_reason=self._disarm_reason,
        )
    

    # ---------------------------------------------------------
    # Simulation Helpers
    # ---------------------------------------------------------

    def set_state(
        self,
        *,
        position=None,
        velocity=None,
        current=None,
        temperature=None,
        bus_voltage=None,
        bus_current=None,
        axis_state=None,
        active_errors=None,
        disarm_reason=None,
    ):
        """
        Update simulated hardware state.

        Returns self so tests may be chained.
        """

        if position is not None:
            self._position = position

        if velocity is not None:
            self._velocity = velocity

        if current is not None:
            self._current = current

        if temperature is not None:
            self._temperature = temperature

        if bus_voltage is not None:
            self._bus_voltage = bus_voltage

        if bus_current is not None:
            self._bus_current = bus_current

        if axis_state is not None:
            self._axis_state = axis_state

        if active_errors is not None:
            self._active_errors = active_errors

        if disarm_reason is not None:
            self._disarm_reason = disarm_reason

        return self
    
    def move_to(
        self,
        position: float,
    ) -> None:
        """
        Simulate moving the actuator to a position.
        """

        self._position = position
        self._commanded_positions.append(position)

    def set_velocity(
        self,
        velocity: float,
    ) -> None:
        """
        Simulate commanding a velocity.
        """

        self._velocity = velocity
        self._commanded_velocities.append(velocity)

    def stop(self) -> None:
        """
        Simulate stopping the actuator.
        """

        self._velocity = 0.0

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def connected(self):
        return self._connected

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    @property
    def current(self):
        return self._current

    @property
    def bus_voltage(self):
        return self._bus_voltage

    @property
    def bus_current(self):
        return self._bus_current

    @property
    def temperature(self):
        return self._temperature

    @property
    def axis_state(self):
        return self._axis_state

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def firmware_version(self):
        return self._firmware_version

    @property
    def active_errors(self):
        return self._active_errors

    @property
    def disarm_reason(self):
        return self._disarm_reason
    
    @property
    def commanded_positions(self):

        return self._commanded_positions
    
    @property
    def commanded_velocities(self):

        return self._commanded_velocities