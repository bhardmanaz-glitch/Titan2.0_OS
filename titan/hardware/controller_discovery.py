from abc import ABC
from abc import abstractmethod


class ControllerDiscovery(ABC):
    """
    Locates physical motor controllers.

    Discovery is intentionally separated from ControllerDriver.
    Controllers should never search for themselves.
    """

    @abstractmethod
    def find(
        self,
        address: str,
    ):
        """
        Locate and return the controller at the requested address.
        """
        pass