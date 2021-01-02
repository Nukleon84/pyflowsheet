from .baseinternal import BaseInternal


class Trays(BaseInternal):
    def __init__(self, start=0, end=1, numberOfTrays=11):
        self.start = start
        self.end = end
        self.numberOfTrays = numberOfTrays
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent

        availableHeight = (unit.size[1] - unit.size[0]) * (self.end - self.start)

        for i in range(self.numberOfTrays):
            if i % 2 == 0:
                xs = unit.position[0]
                xe = unit.position[0] + unit.size[0] * 0.8
            else:
                xs = unit.position[0] + unit.size[0] * 0.2
                xe = unit.position[0] + unit.size[0]

            ctx.line(
                (
                    xs,
                    unit.position[1]
                    + unit.size[0] / 2
                    + availableHeight * self.start
                    + availableHeight / self.numberOfTrays * i,
                ),
                (
                    xe,
                    unit.position[1]
                    + unit.size[0] / 2
                    + availableHeight * self.start
                    + availableHeight / self.numberOfTrays * i,
                ),
                unit.lineColor,
                unit.lineSize,
            )

        return