from .baseinternal import BaseInternal


class Tubes(BaseInternal):
    def __init__(self, numberOfTubes=5, numberOfPasses=1):
        self.numberOfPasses = numberOfPasses
        self.numberOfTubes = numberOfTubes
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

        for i in range(1, self.numberOfTubes):
            x = unit.position[0] + unit.size[0] / self.numberOfTubes * i
            start = (x, unit.position[1] + capLength)
            end = (x, unit.position[1] + unit.size[1] - capLength)
            ctx.line(start, end, unit.lineColor, unit.lineSize)

        for p in range(1, self.numberOfPasses):
            x = unit.position[0] + unit.size[0] - p * unit.size[0] / self.numberOfPasses
            if p % 2 == 1:
                start = (x, unit.position[1] + capLength)
                end = (x, unit.position[1] + capLength / 2)
                ctx.line(start, end, unit.lineColor, unit.lineSize)

                start = (x, unit.position[1] + unit.size[1])
                end = (x, unit.position[1] + unit.size[1] - capLength)
                ctx.line(start, end, unit.lineColor, unit.lineSize)
            if p % 2 == 0:
                start = (x, unit.position[1])
                end = (x, unit.position[1] + capLength)
                ctx.line(start, end, unit.lineColor, unit.lineSize)

                start = (x, unit.position[1] + unit.size[1] - capLength)
                end = (x, unit.position[1] + unit.size[1] - capLength / 2)
                ctx.line(start, end, unit.lineColor, unit.lineSize)

        return