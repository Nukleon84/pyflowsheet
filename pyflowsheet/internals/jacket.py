from .baseinternal import BaseInternal


class Jacket(BaseInternal):
    def __init__(self, thickness=5):
        self.thickness = thickness
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

        bevelLength = self.thickness * 2

        ctx.path(
            [
                (
                    unit.position[0],
                    unit.position[1] + unit.size[1] / 2 + bevelLength,
                ),
                (
                    unit.position[0] - self.thickness,
                    unit.position[1] + unit.size[1] / 2 + 2 * bevelLength,
                ),
                (
                    unit.position[0] - self.thickness,
                    unit.position[1] + unit.size[1] - capLength,
                ),
            ],
            None,
            unit.lineColor,
            unit.lineSize,
        )

        ctx.path(
            [
                (
                    unit.position[0] + unit.size[0],
                    unit.position[1] + unit.size[1] / 2 + bevelLength,
                ),
                (
                    unit.position[0] + unit.size[0] + self.thickness,
                    unit.position[1] + unit.size[1] / 2 + 2 * bevelLength,
                ),
                (
                    unit.position[0] + unit.size[0] + self.thickness,
                    unit.position[1] + unit.size[1] - capLength,
                ),
            ],
            None,
            unit.lineColor,
            unit.lineSize,
        )

        ctx.chord(
            [
                (
                    unit.position[0] - self.thickness,
                    unit.position[1] + unit.size[1] - 2 * capLength - self.thickness,
                ),
                (
                    unit.position[0] + unit.size[0] + self.thickness,
                    unit.position[1] + unit.size[1] + self.thickness,
                ),
            ],
            0,
            180,
            None,
            unit.lineColor,
            unit.lineSize,
            closePath=False,
        )
        # ctx.chord(
        #     [
        #         (
        #             unit.position[0] - self.thickness,
        #             unit.position[1] + unit.size[1] - 2 * capLength - self.thickness,
        #         ),
        #         (
        #             unit.position[0] + unit.size[0] + self.thickness,
        #             unit.position[1] + unit.size[1] + self.thickness,
        #         ),
        #     ],
        #     100,
        #     180,
        #     None,
        #     unit.lineColor,
        #     unit.lineSize,
        #     closePath=False,
        # )

        # ctx.path(
        #     [
        #         (
        #             unit.position[0] + unit.size[0] / 2 - 9,
        #             unit.position[1] + unit.size[1] + self.thickness - 1,
        #         ),
        #         (
        #             unit.position[0] + unit.size[0] / 2,
        #             unit.position[1] + unit.size[1],
        #         ),
        #         (
        #             unit.position[0] + unit.size[0] / 2 + 9,
        #             unit.position[1] + unit.size[1] + self.thickness - 1,
        #         ),
        #     ],
        #     None,
        #     unit.lineColor,
        #     unit.lineSize,
        # )

        return