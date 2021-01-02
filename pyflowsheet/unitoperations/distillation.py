from ..core import UnitOperation
from ..core import Port


class Distillation(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        hasCondenser=True,
        hasReboiler=True,
        position=(0, 0),
        size=(40, 200),
        description: str = "",
        internals=[],
    ):

        super().__init__(id, name, position=position, size=size, internals=internals)

        self.hasReboiler = hasReboiler
        self.hasCondenser = hasCondenser

        if self.hasReboiler:
            self.textOffset = (0, self.size[0])
        else:
            self.textOffset = (0, 20)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["Feed"] = Port("Feed", self, (0, 0.5), (-1, 0))

        if self.hasCondenser:
            self.ports["Top"] = Port(
                "Top",
                self,
                (2.0, self.size[0] / 2 / self.size[1]),
                (1, 0),
                intent="out",
            )
        else:
            self.ports["VOut"] = Port("VOut", self, (0.5, 0), (0, -1), intent="out")
            self.ports["RIn"] = Port(
                "RIn", self, (1.0, self.size[0] / 2 / self.size[1]), (1, 0)
            )

        if self.hasReboiler:
            self.ports["Bottom"] = Port(
                "Bottom",
                self,
                (2.0, 1 + self.size[0] / 2 / self.size[1]),
                (1, 0),
                intent="out",
            )
        else:
            self.ports["LOut"] = Port("LOut", self, (0.5, 1), (0, 1), intent="out")
            self.ports["VIn"] = Port(
                "VIn", self, (1.0, 1 - self.size[0] / 2 / self.size[1]), (1, 0)
            )

        return

    def intersectsPoint(self, point):
        minx = self.position[0]
        miny = self.position[1]
        maxx = self.position[0] + self.size[0]
        maxy = self.position[1] + self.size[1]

        if self.hasCondenser:
            miny -= self.size[0]
            maxx = self.position[0] + self.size[0] + self.size[0]
        if self.hasReboiler:
            maxy += self.size[0]
            maxx = self.position[0] + self.size[0] + self.size[0]

        test_x = point[0] >= minx and point[0] <= maxx
        test_y = point[1] >= miny and point[1] <= maxy
        return test_x and test_y

    def draw(self, ctx):

        if self.hasCondenser == True:
            self._drawCondenser(ctx)

        if self.hasReboiler == True:
            self._drawReboiler(ctx)

        self._drawBasicShape(ctx)

        super().draw(ctx)

        return

    def _drawBasicShape(self, ctx):
        ctx.chord(
            [
                (self.position[0], self.position[1]),
                (self.position[0] + self.size[0], self.position[1] + self.size[0]),
            ],
            180,
            360,
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

        ctx.rectangle(
            [
                (self.position[0], self.position[1] + self.size[0] / 2),
                (
                    self.position[0] + self.size[0],
                    self.position[1] + self.size[1] - self.size[0] / 2,
                ),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

        ctx.chord(
            [
                (self.position[0], self.position[1] + self.size[1] - self.size[0]),
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
            ],
            0,
            180,
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

    def _drawReboiler(self, ctx):
        ctx.rectangle(
            [
                (
                    self.position[0] + self.size[0] / 2,
                    self.position[1] + self.size[1] - self.size[0] / 2,
                ),
                (
                    self.position[0] + 3 * self.size[0] / 2,
                    self.position[1] + self.size[1] + self.size[0] / 2,
                ),
            ],
            None,
            self.lineColor,
            self.lineSize,
        )
        ctx.circle(
            [
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
                (
                    self.position[0] + 2 * self.size[0],
                    self.position[1] + self.size[1] + self.size[0],
                ),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

    def _drawCondenser(self, ctx):
        ctx.rectangle(
            [
                (
                    self.position[0] + self.size[0] / 2,
                    self.position[1] - self.size[0] / 2,
                ),
                (
                    self.position[0] + 3 * self.size[0] / 2,
                    self.position[1] + self.size[0] / 2,
                ),
            ],
            None,
            self.lineColor,
            self.lineSize,
        )
        ctx.circle(
            [
                (self.position[0] + self.size[0], self.position[1] - self.size[0]),
                (self.position[0] + 2 * self.size[0], self.position[1]),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )
        ctx.line(
            (
                self.position[0] + 3 * self.size[0] / 2,
                self.position[1] + self.size[0] / 2,
            ),
            (
                self.position[0] + 2 * self.size[0],
                self.position[1] + self.size[0] / 2,
            ),
            self.lineColor,
            self.lineSize,
        )
