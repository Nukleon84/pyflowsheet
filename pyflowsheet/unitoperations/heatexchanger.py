from ..core import UnitOperation
from ..core import Port


class HeatExchanger(UnitOperation):
    def __init__(
        self, id: str, name: str, position=(0, 0), size=(40, 40), description: str = ""
    ):
        super().__init__(id, name, position=position, size=size)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["TIn"] = Port("TIn", self, (0, 0.5), (-1, 0))
        self.ports["TOut"] = Port("TOut", self, (1, 0.5), (1, 0), intent="out")

        self.ports["SIn"] = Port("SIn", self, (0.5, 0), (0, -1))
        self.ports["SOut"] = Port("SOut", self, (0.5, 1), (0, 1), intent="out")

        return

    def draw(self, ctx):

        ctx.circle(
            [
                self.position,
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )

        vfrac = 1 / 4
        hfrac = 1 / 3
        hfrac2 = 1 / 6

        points = []

        points.append((self.position[0], self.position[1] + self.size[1] * 0.5))
        points.append(
            (
                self.position[0] + self.size[0] * hfrac2,
                self.position[1] + self.size[1] * 0.5,
            )
        )
        points.append(
            (
                self.position[0] + self.size[0] * hfrac,
                self.position[1] + self.size[1] * (0.5 - vfrac),
            )
        )
        points.append(
            (
                self.position[0] + self.size[0] * 2 * hfrac,
                self.position[1] + self.size[1] * (0.5 + vfrac),
            )
        )
        points.append(
            (
                self.position[0] + self.size[0] * (1 - hfrac2),
                self.position[1] + self.size[1] * 0.5,
            )
        )
        points.append(
            (self.position[0] + self.size[0], self.position[1] + self.size[1] * 0.5)
        )

        ctx.path(points, None, self.lineColor, self.lineSize, close=False)

        super().draw(ctx)

        return