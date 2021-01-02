from ..core import UnitOperation
from ..core import Port


class Vessel(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        position=(0, 0),
        size=(40, 100),
        description: str = "",
        capLength=None,
        internals=[],
        angle=0,
        showCapLines=True,
    ):

        super().__init__(id, name, position=position, size=size, internals=internals)

        self.capLength = capLength
        self.showCapLines = showCapLines
        self.updatePorts()
        self.rotate(angle)

    def updatePorts(self):
        self.ports = {}

        self.ports["In"] = Port("In", self, (0.5, 1), (0, 1))
        self.ports["Out"] = Port("Out", self, (0.5, 0), (0, -1), intent="out")

    def _drawBasicShape(self, ctx):
        if self.capLength == None:
            capLength = self.size[0] / 2
        else:
            capLength = self.capLength

        ctx.rectangle(
            [
                (self.position[0], self.position[1] + capLength),
                (
                    self.position[0] + self.size[0],
                    self.position[1] + self.size[1] - capLength,
                ),
            ],
            self.fillColor,
            self.fillColor,
            self.lineSize,
        )

        ctx.line(
            (self.position[0], self.position[1] + capLength),
            (
                self.position[0],
                self.position[1] + self.size[1] - capLength,
            ),
            self.lineColor,
            self.lineSize,
        )
        ctx.line(
            (self.position[0] + self.size[0], self.position[1] + capLength),
            (
                self.position[0] + self.size[0],
                self.position[1] + self.size[1] - capLength,
            ),
            self.lineColor,
            self.lineSize,
        )

        ctx.chord(
            [
                (self.position[0], self.position[1]),
                (self.position[0] + self.size[0], self.position[1] + 2 * capLength),
            ],
            180,
            360,
            self.fillColor,
            self.lineColor,
            self.lineSize,
            closePath=self.showCapLines,
        )

        ctx.chord(
            [
                (self.position[0], self.position[1] + self.size[1] - 2 * capLength),
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
            ],
            0,
            180,
            self.fillColor,
            self.lineColor,
            self.lineSize,
            closePath=self.showCapLines,
        )

        return

    def draw(self, ctx):

        self._drawBasicShape(ctx)

        super().draw(ctx)
        return