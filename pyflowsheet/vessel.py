from .unitoperation import UnitOperation
from .port import Port


class Vessel(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        orientation="vertical",
        position=(0, 0),
        size=(40, 100),
        description: str = "",
        capLength=None,
        internals=None,
    ):

        super().__init__(id, name, position=position, size=size)

        self.orientation = orientation
        self.internals = internals
        self.capLength = capLength
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}

        if self.orientation.lower() == "vertical":
            self.ports["In"] = Port("In", self, (0.5, 1), (0, 1))
            self.ports["Out"] = Port("Out", self, (0.5, 0), (0, -1), intent="out")
        if self.orientation.lower() == "horizontal":
            self.ports["In"] = Port("In", self, (0, 0.5), (-1, 0))
            self.ports["Out"] = Port("Out", self, (1, 0.5), (1, 0), intent="out")

    def _drawVertical(self, ctx):
        if self.capLength == None:
            capLength = self.size[0] / 2
        else:
            capLength = self.capLength

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
        )

        ctx.rectangle(
            [
                (self.position[0], self.position[1] + capLength),
                (
                    self.position[0] + self.size[0],
                    self.position[1] + self.size[1] - capLength,
                ),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
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
        )
        if self.internals and self.internals.lower() == "tubes":
            for i in range(1, 5):
                x = self.position[0] + self.size[0] / 5 * i
                start = (x, self.position[1] + capLength)
                end = (x, self.position[1] + self.size[1] - capLength)
                ctx.line(start, end, self.lineColor, self.lineSize)

        if self.internals and self.internals.lower() == "bed":
            start = (self.position[0], self.position[1] + capLength)
            end = (
                self.position[0] + self.size[0],
                self.position[1] + self.size[1] - capLength,
            )
            ctx.line(start, end, self.lineColor, self.lineSize)

            start = (self.position[0] + self.size[0], self.position[1] + capLength)
            end = (self.position[0], self.position[1] + self.size[1] - capLength)
            ctx.line(start, end, self.lineColor, self.lineSize)
        return

    def _drawHorizontal(self, ctx):
        if self.capLength == None:
            capLength = self.size[1] / 2
        else:
            capLength = self.capLength

        ctx.chord(
            [
                (self.position[0], self.position[1]),
                (self.position[0] + 2 * capLength, self.position[1] + self.size[1]),
            ],
            90,
            270,
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

        ctx.rectangle(
            [
                (self.position[0] + capLength, self.position[1]),
                (
                    self.position[0] + self.size[0] - capLength,
                    self.position[1] + self.size[1],
                ),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

        ctx.chord(
            [
                (self.position[0] + self.size[0] - 2 * capLength, self.position[1]),
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
            ],
            270,
            90,
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )
        if self.internals and self.internals.lower() == "tubes":
            for i in range(1, 5):
                y = self.position[1] + self.size[1] / 5 * i
                start = (self.position[0] + capLength, y)
                end = (self.position[0] + self.size[0] - capLength, y)
                ctx.line(start, end, self.lineColor, self.lineSize)

        if self.internals and self.internals.lower() == "bed":
            start = (self.position[0] + capLength, self.position[1])
            end = (
                self.position[0] + self.size[0] - capLength,
                self.position[1] + self.size[1],
            )
            ctx.line(start, end, self.lineColor, self.lineSize)

            start = (self.position[0] + capLength, self.position[1] + self.size[1])
            end = (self.position[0] + self.size[0] - capLength, self.position[1])
            ctx.line(start, end, self.lineColor, self.lineSize)
        return

    def draw(self, ctx):

        if self.orientation.lower() == "vertical":
            self._drawVertical(ctx)

        if self.orientation.lower() == "horizontal":
            self._drawHorizontal(ctx)

        super().draw(ctx)
        return