from .unitoperation import UnitOperation
from .port import Port


class Valve(UnitOperation):
    def __init__(
        self, id: str, name: str, position=(0, 0), size=(40, 20), description: str = ""
    ):
        super().__init__(id, name, position=position, size=size)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["In"] = Port("In", self, (0, 0.5), (-1, 0))
        self.ports["Out"] = Port("Out", self, (1, 0.5), (1, 0), intent="out")
        return

    def draw(self, ctx):
        points = []

        points.append((self.position[0], self.position[1]))
        points.append(
            (self.position[0] + self.size[0], self.position[1] + self.size[1])
        )
        points.append((self.position[0] + self.size[0], self.position[1]))
        points.append((self.position[0], self.position[1] + self.size[1]))

        ctx.path(points, self.fillColor, self.lineColor, self.lineSize, close=True)

        super().draw(ctx)

        return