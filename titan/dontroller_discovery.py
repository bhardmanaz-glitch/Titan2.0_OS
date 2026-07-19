from abc import ABC, abstractmethod

from titan.hardware.controller_driver import ControllerDriver


class ControllerDiscovery(ABC):

    @abstractmethod
    def find(
        self,
        address: str,
    ) -> ControllerDriver:
        """
        Locate a controller by its transport-specific address.
        """
        pass

    @abstractmethod
    def enumerate(self) -> list[ControllerDriver]:
        """
        Return every controller currently visible.
        """
        pass

    @abstractmethod
    def list_addresses(self) -> list[str]:
        """
        Convenience helper for diagnostics.
        """
        pass