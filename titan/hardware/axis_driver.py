"""
Titan 2.0 Operating System

Hardware Interface Layer

Abstract axis driver interface.

Every physical motor controller (ODrive, MKS, etc.)
must implement this interface.
"""

from abc import ABC, abstractmethod


class AxisDriver(ABC):
    """Abstract hardware interface for a single motor axis."""

    @property
    @abstractmethod
    def connected(self) -> bool:
        ...

    @property
    @abstractmethod
    def serial_number(self) -> str:
        ...

    @property
    @abstractmethod
    def firmware_version(self) -> str:
        ...

    @property
    @abstractmethod
    def bus_voltage(self) -> float:
        ...

    @property
    @abstractmethod
    def bus_current(self) -> float:
        ...

    @property
    @abstractmethod
    def position(self) -> float:
        ...

    @property
    @abstractmethod
    def velocity(self) -> float:
        ...

    @property
    @abstractmethod
    def current(self) -> float:
        ...

    @property
    @abstractmethod
    def temperature(self) -> float:
        ...

    @property
    @abstractmethod
    def axis_state(self) -> str:
        ...

    @property
    @abstractmethod
    def active_errors(self):
        ...

    @property
    @abstractmethod
    def disarm_reason(self):
        ...

    @abstractmethod
    def connect(self) -> None:
        ...

    @abstractmethod
    def disconnect(self) -> None:
        ...

    @abstractmethod
    def refresh(self) -> None:
        ...

    @abstractmethod
    def move_to(self, position: float) -> None:
        """
        Command the actuator to move to a position.
        """
        ...

    @abstractmethod
    def set_velocity(self, velocity: float) -> None:
        """
        Command the actuator to a velocity.
        """
        ...

    @abstractmethod
    def stop(self) -> None:
        """
        Stop actuator motion safely.
        """
        ...