from ..core import UnitOperation
from ..core import Port

from ..core.enums import FlowPattern


class PlateHex(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        position=(0, 0),
        size=(40, 80),
        description: str = "",
        pattern=FlowPattern.CounterCurrent,
    ):
        super().__init__(id, name, position=position, size=size)
        self.pattern = pattern
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        if self.pattern == FlowPattern.CounterCurrent:
            self.addPort(Port("In1", self, (0, 0.875), (-1, 0)))
            self.addPort(Port("In2", self, (1, 0.875), (1, 0)))
            self.addPort(Port("Out1", self, (1, 0.125), (1, 0), intent="out"))
            self.addPort(Port("Out2", self, (0, 0.125), (-1, 0), intent="out"))
        else:
            self.addPort(Port("In1", self, (0, 0.875), (-1, 0)))
            self.addPort(Port("In2", self, (0, 0.125), (-1, 0)))
            self.addPort(Port("Out1", self, (1, 0.125), (1, 0), intent="out"))
            self.addPort(Port("Out2", self, (1, 0.875), (1, 0), intent="out"))
        return

    def draw(self, ctx):

        ctx.rectangle(
            [
                self.position,
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

        ctx.line(
            (self.position[0], self.position[1] + 0.875 * self.size[1]),
            (
                self.position[0] + self.size[0],
                self.position[1] + 0.125 * self.size[1],
            ),
            self.lineColor,
            self.lineSize,
        )

        ctx.line(
            (self.position[0], self.position[1] + 0.125 * self.size[1]),
            (
                self.position[0] + self.size[0],
                self.position[1] + 0.875 * self.size[1],
            ),
            self.lineColor,
            self.lineSize,
        )

        availableHeight = self.size[1] * (0.7 - 0.3)

        for i in range(3):
            y = self.position[1] + self.size[1] * 0.3 + availableHeight / 2 * i
            ctx.line(
                (self.position[0], y),
                (
                    self.position[0] + self.size[0],
                    y,
                ),
                self.lineColor,
                self.lineSize,
            )

        super().draw(ctx)

        return