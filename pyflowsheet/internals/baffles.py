from .baseinternal import BaseInternal


class Baffles(BaseInternal):
    def __init__(self, start=0, end=1, numberOfBaffles=11):
        self.start = start
        self.end = end
        self.numberOfBaffles = numberOfBaffles
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent
        if unit.capLength == None:
            capLength = unit.size[0] / 2
        else:
            capLength = unit.capLength

        availableHeight = (unit.size[1] - 2 * capLength) * (self.end - self.start)

        for i in range(self.numberOfBaffles):
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
                    + capLength
                    + availableHeight * self.start
                    + availableHeight / self.numberOfBaffles * i,
                ),
                (
                    xe,
                    unit.position[1]
                    + capLength
                    + availableHeight * self.start
                    + availableHeight / self.numberOfBaffles * i,
                ),
                unit.lineColor,
                unit.lineSize,
            )

        return