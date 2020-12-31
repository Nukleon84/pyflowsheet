from ..core import UnitOperation
from ..core import Port


class StreamFlag(UnitOperation):
    def __init__(
        self, id: str, name: str, position=(0, 0), size=(40, 40), description: str = ""
    ):
        super().__init__(id, name, position=position, size=size)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["In"] = Port("In", self, (0, 0.5), (-1, 0))
        self.ports["Out"] = Port("Out", self, (1, 0.5), (1, 0), intent="out")
        return

    def draw(self, ctx):

        vfrac = 1 / 4
        hfrac = 1 / 2

        points = []

        points.append((self.position[0], self.position[1] + self.size[1] * vfrac))
        points.append(
            (
                self.position[0] + self.size[0] * hfrac,
                self.position[1] + self.size[1] * vfrac,
            )
        )
        points.append((self.position[0] + self.size[0] * hfrac, self.position[1]))
        points.append(
            (self.position[0] + self.size[0], self.position[1] + self.size[1] / 2)
        )
        points.append(
            (self.position[0] + self.size[0] * hfrac, self.position[1] + self.size[1])
        )
        points.append(
            (
                self.position[0] + self.size[0] * hfrac,
                self.position[1] + self.size[1] * (1 - vfrac),
            )
        )
        points.append((self.position[0], self.position[1] + self.size[1] * (1 - vfrac)))

        ctx.path(points, self.fillColor, self.lineColor, self.lineSize, close=True)

        super().draw(ctx)

        return