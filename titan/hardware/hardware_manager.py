class HardwareManager:

    def __init__(self):

        self.axes = {}

    def add_axis(self, name, axis):

        self.axes[name] = axis

    def connect(self):

        for axis in self.axes.values():
            axis.connect()

    def disconnect(self):

        for axis in self.axes.values():
            axis.disconnect()

    def refresh(self):

        return {
        name: axis.refresh()
        for name, axis in self.axes.items()
        }