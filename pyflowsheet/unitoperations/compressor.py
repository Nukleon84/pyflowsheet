from ..core import UnitOperation
from ..core import Port
from math import sin, cos, radians, sqrt


class Compressor(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        position=(0, 0),
        size=(40, 40),
        description: str = "",
        internals=[],
    ):
        super().__init__(id, name, position=position, size=size, internals=internals)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["In"] = Port("In", self, (0, 0.5), (-1, 0))
        self.ports["Out"] = Port("Out", self, (1, 0.5), (1, 0), intent="out")
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

        radiansOfStartingAngle = radians(120)
        dxs = self.size[0] / 2 * cos(radiansOfStartingAngle)
        dys = self.size[0] / 2 * sin(radiansOfStartingAngle)

        start_up = (
            self.position[0] + self.size[0] / 2 + dxs,
            self.position[1] + self.size[1] / 2 - dys,
        )
        start_low = (
            self.position[0] + self.size[0] / 2 + dxs,
            self.position[1] + self.size[1] / 2 + dys,
        )

        radiansOfEndingAngle = radians(10)
        dx = self.size[0] / 2 * cos(radiansOfEndingAngle)
        dy = self.size[0] / 2 * sin(radiansOfEndingAngle)

        end_up = (
            self.position[0] + self.size[0] / 2 + dx,
            self.position[1] + self.size[1] / 2 - dy,
        )
        end_low = (
            self.position[0] + self.size[0] / 2 + dx,
            self.position[1] + self.size[1] / 2 + dy,
        )

        ctx.line(start_up, end_up, self.lineColor, self.lineSize)
        ctx.line(start_low, end_low, self.lineColor, self.lineSize)

        super().draw(ctx)

        return