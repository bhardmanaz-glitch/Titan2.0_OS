"""
Titan 2.0 Operating System

Hardware Manager

Central manager responsible for connecting, tracking,
refreshing, and disconnecting robot hardware.
"""
from titan.hardware.controller_factory import ControllerFactory
from titan.hardware.hardware_inventory import JointHardware
from titan.hardware.odrive_axis import ODriveAxis

from titan.hardware.axis_factory import AxisFactory

class HardwareManager:
    """
    Manages all hardware currently connected to Titan.
    """

    def __init__(self):

        self.controllers = {}

        self.axes = {}

    def _get_controller(
        self,
        hardware: JointHardware,
    ):

        address = hardware.controller_address

        if address in self.controllers:

            return self.controllers[address]

        controller = ControllerFactory.create(
            hardware
        )

        controller.connect()

        self.controllers[address] = controller

        return controller

    def connect_joint(
        self,
        hardware: JointHardware,
    ):

        controller = self._get_controller(
            hardware
        )

        axis = AxisFactory.create(
            hardware,
            controller,
        )

        axis.connect()

        self.axes[hardware.identifier] = axis

        return axis 

    def add_axis(
        self,
        name: str,
        axis: ODriveAxis,
    ):

        self.axes[name] = axis

    def get_axis(
        self,
        name: str,
    ) -> ODriveAxis:

        return self.axes[name]

    def disconnect(self):

        for axis in self.axes.values():
            axis.disconnect()

        self.axes.clear()

    def refresh(self):

        return {
            name: axis.refresh()
            for name, axis in self.axes.items()
        }