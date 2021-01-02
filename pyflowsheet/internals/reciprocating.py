from .baseinternal import BaseInternal


class Reciprocating(BaseInternal):
    def __init__(self):
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent

        ctx.line(
            (
                unit.position[0] + unit.size[0] * 0.4,
                unit.position[1] + unit.size[1] / 2,
            ),
            (
                unit.position[0] + unit.size[0] * 0.8,
                unit.position[1] + unit.size[1] / 2,
            ),
            unit.lineColor,
            unit.lineSize,
        )
        ctx.line(
            (
                unit.position[0] + unit.size[0] * 0.4,
                unit.position[1] + unit.size[1] * 0.3,
            ),
            (
                unit.position[0] + unit.size[0] * 0.4,
                unit.position[1] + unit.size[1] * 0.7,
            ),
            unit.lineColor,
            unit.lineSize,
        )

        return