from .unitoperation import UnitOperation
from .port import Port


class Mixer(UnitOperation):
    def __init__(
        self, id: str, name: str, position=(0, 0), size=(20, 20), description: str = ""
    ):
        super().__init__(id, name, position=position, size=size)
        self.fillColor = (0, 0, 0, 255)
        self.lineColor = (0, 0, 0, 255)
        self.textOffset = (0, 10)
        self.updatePorts()

    def updatePorts(self):
        self.ports = {}
        self.ports["In1"] = Port("In1", self, (0.2, 0.5), (-1, 0))
        self.ports["In2"] = Port("In2", self, (0.5, 0.2), (0, -1))
        self.ports["In3"] = Port("In3", self, (0.5, 0.8), (0, 1))
        self.ports["Out"] = Port("Out", self, (0.8, 0.5), (1, 0), intent="out")
        return

    def draw(self, ctx):

        ctx.rectangle(
            [
                (self.position[0] + 5, self.position[1] + 5),
                (
                    self.position[0] + self.size[0] - 5,
                    self.position[1] + self.size[1] - 5,
                ),
            ],
            self.fillColor,
            self.lineColor,
            self.lineSize,
        )
        # ctx.line(
        #     (self.position[0], self.position[1] + self.size[1] / 2),
        #     (self.position[0] + self.size[0], self.position[1] + self.size[1] / 2),
        #     self.lineColor,
        #     self.lineSize,
        # )
        # ctx.line(
        #     (self.position[0] + self.size[0] / 2, self.position[1]),
        #     (self.position[0] + self.size[0] / 2, self.position[1] + self.size[1]),
        #     self.lineColor,
        #     self.lineSize,
        # )

        super().draw(ctx)

        return