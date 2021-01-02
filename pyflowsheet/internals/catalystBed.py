from .baseinternal import BaseInternal


class CatalystBed(BaseInternal):
    def __init__(self):
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

        start = (unit.position[0], unit.position[1] + capLength)
        end = (
            unit.position[0] + unit.size[0],
            unit.position[1] + unit.size[1] - capLength,
        )
        ctx.line(start, end, unit.lineColor, unit.lineSize)

        start = (unit.position[0] + unit.size[0], unit.position[1] + capLength)
        end = (unit.position[0], unit.position[1] + unit.size[1] - capLength)
        ctx.line(start, end, unit.lineColor, unit.lineSize)

        return