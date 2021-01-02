from .baseinternal import BaseInternal


class DividingWall(BaseInternal):
    def __init__(self):
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent

        ctx.line(
            (unit.position[0] + unit.size[0] / 2, unit.position[1] + unit.size[0]),
            (
                unit.position[0] + unit.size[0] / 2,
                unit.position[1] + unit.size[1] - unit.size[0],
            ),
            unit.lineColor,
            unit.lineSize,
        )

        return