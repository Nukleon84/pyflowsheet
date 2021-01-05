from enum import Enum, auto


class HorizontalLabelAlignment(Enum):
    LeftOuter = auto()
    Left = auto()
    Center = auto()
    Right = auto()
    RightOuter = auto()


class VerticalLabelAlignment(Enum):
    Top = auto()
    Center = auto()
    Bottom = auto()


class FlowPattern(Enum):
    CoCurrent = auto()
    CounterCurrent = auto()