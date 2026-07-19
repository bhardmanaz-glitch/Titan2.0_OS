from abc import ABC, abstractmethod

from titan.hardware.telemetry import Telemetry


class ControllerDriver(ABC):
    """
    Hardware interface for a single motor controller.

    Every hardware implementation (ODrive USB, ODrive CAN,
    MKS CAN, Simulation, etc.) must implement this contract.
    """

    # --------------------------------------------------
    # Connection
    # --------------------------------------------------

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @property
    @abstractmethod
    def connected(self) -> bool:
        pass

    # --------------------------------------------------
    # Motion
    # --------------------------------------------------

    @abstractmethod
    def enter_closed_loop(self) -> None:
        pass

    @abstractmethod
    def enter_idle(self) -> None:
        pass

    @abstractmethod
    def move_to(
        self,
        position: float,
    ) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def set_velocity(
        self,
        velocity: float,
    ) -> None:
        pass

    # --------------------------------------------------
    # Telemetry
    # --------------------------------------------------

    @abstractmethod
    def refresh(self) -> Telemetry:
        """
        Read hardware and return a telemetry snapshot.
        """
        pass