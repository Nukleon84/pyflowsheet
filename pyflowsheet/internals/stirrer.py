from .baseinternal import BaseInternal
from enum import Enum, auto


class StirrerType(Enum):
    Propeller = auto()
    Anchor = auto()
    Helical = auto()


class Stirrer(BaseInternal):
    def __init__(self, type=StirrerType.Propeller):
        self.type = type
        return

    def draw(self, ctx):
        if self.parent is None:
            Warning("Internal has no parent set!")
            return

        unit = self.parent

        ctx.line(
            (unit.position[0] + unit.size[0] / 2, unit.position[1]),
            (
                unit.position[0] + unit.size[0] / 2,
                unit.position[1] + unit.size[1] - unit.size[0] / 2,
            ),
            unit.lineColor,
            unit.lineSize,
        )

        bladeLength = unit.size[0] / 4
        bladeHeight = unit.size[1] / 20

        if self.type == StirrerType.Anchor:
            ctx.line(
                (
                    unit.position[0] + unit.size[0] / 2 - bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2,
                ),
                (
                    unit.position[0] + unit.size[0] / 2 + bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2,
                ),
                unit.lineColor,
                unit.lineSize,
            )
            ctx.line(
                (
                    unit.position[0] + unit.size[0] / 2 - bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2,
                ),
                (
                    unit.position[0] + unit.size[0] / 2 - bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2 - bladeHeight,
                ),
                unit.lineColor,
                unit.lineSize,
            )
            ctx.line(
                (
                    unit.position[0] + unit.size[0] / 2 + bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2,
                ),
                (
                    unit.position[0] + unit.size[0] / 2 + bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2 - bladeHeight,
                ),
                unit.lineColor,
                unit.lineSize,
            )
        if self.type == StirrerType.Propeller:
            ctx.line(
                (
                    unit.position[0] + unit.size[0] / 2 - bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2,
                ),
                (
                    unit.position[0] + unit.size[0] / 2 + bladeLength,
                    unit.position[1] + unit.size[1] - unit.size[0] / 2,
                ),
                unit.lineColor,
                unit.lineSize,
            )
            ctx.rectangle(
                [
                    (
                        unit.position[0] + unit.size[0] / 2 - bladeLength,
                        unit.position[1]
                        + unit.size[1]
                        - unit.size[0] / 2
                        - bladeHeight,
                    ),
                    (
                        unit.position[0] + unit.size[0] / 2 - 0.5 * bladeLength,
                        unit.position[1]
                        + unit.size[1]
                        - unit.size[0] / 2
                        + bladeHeight,
                    ),
                ],
                unit.lineColor,
                unit.lineColor,
                unit.lineSize,
            )
            ctx.rectangle(
                [
                    (
                        unit.position[0] + unit.size[0] / 2 + 0.5 * bladeLength,
                        unit.position[1]
                        + unit.size[1]
                        - unit.size[0] / 2
                        - bladeHeight,
                    ),
                    (
                        unit.position[0] + unit.size[0] / 2 + bladeLength,
                        unit.position[1]
                        + unit.size[1]
                        - unit.size[0] / 2
                        + bladeHeight,
                    ),
                ],
                unit.lineColor,
                unit.lineColor,
                unit.lineSize,
            )

        return