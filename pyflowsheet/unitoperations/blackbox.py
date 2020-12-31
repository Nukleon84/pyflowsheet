from ..core import UnitOperation
from ..core import Port


class BlackBox(UnitOperation):
    def __init__(
        self, id: str, name: str, position=(0, 0), size=(20, 20), description: str = ""
    ):
        super().__init__(id, name, position=position, size=size)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["In"] = Port("In", self, (0, 0.5), (-1, 0))
        self.ports["Out"] = Port("Out", self, (1, 0.5), (1, 0), intent="out")
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

        super().draw(ctx)

        return