from .baseinternal import BaseInternal
from math import sin, cos, radians, sqrt


class LiquidRing(BaseInternal):
    def __init__(self):
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent

        lines = 4
        bladeLength = unit.size[0] / 2 * 0.5

        for i in range(lines):
            angle = 180 / lines * i
            angleInRadians = radians(angle)
            dxs = bladeLength * cos(angleInRadians)
            dys = bladeLength * sin(angleInRadians)

            ctx.line(
                (
                    unit.position[0] + unit.size[0] / 2 + dxs,
                    unit.position[1] + unit.size[1] / 2 + dys,
                ),
                (
                    unit.position[0] + unit.size[0] / 2 - dxs,
                    unit.position[1] + unit.size[1] / 2 - dys,
                ),
                unit.lineColor,
                unit.lineSize / 2,
            )

        return