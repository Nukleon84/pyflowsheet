from .baseinternal import BaseInternal


class RandomPacking(BaseInternal):
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent

        availableHeight = unit.size[1] - unit.size[0]

        ctx.line(
            (
                unit.position[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.start,
            ),
            (
                unit.position[0] + unit.size[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.end,
            ),
            unit.lineColor,
            unit.lineSize,
        )

        ctx.line(
            (
                unit.position[0] + unit.size[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.start,
            ),
            (
                unit.position[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.end,
            ),
            unit.lineColor,
            unit.lineSize,
        )

        # horizontal line top
        ctx.line(
            (
                unit.position[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.start,
            ),
            (
                unit.position[0] + unit.size[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.start,
            ),
            unit.lineColor,
            unit.lineSize,
        )
        # horizontal line bottom
        ctx.line(
            (
                unit.position[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.end,
            ),
            (
                unit.position[0] + unit.size[0],
                unit.position[1] + unit.size[0] / 2 + availableHeight * self.end,
            ),
            unit.lineColor,
            unit.lineSize,
        )

        return