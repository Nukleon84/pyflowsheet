from .enums import HorizontalLabelAlignment, VerticalLabelAlignment
from math import sin, cos, radians, sqrt


class UnitOperation(object):
    def __init__(
        self, id: str, name: str, position=(0, 0), size=(20, 20), description: str = ""
    ):
        self.id = id
        self.name = name
        self.description = description
        self.lineColor = (0, 0, 0, 255)
        self.fillColor = (255, 255, 255, 255)
        self.textColor = (0, 0, 0, 255)
        self.size = size
        self.position = position
        self.lineSize = 2
        self.drawBoundingBox = False
        self.verticalLabelAlignment = VerticalLabelAlignment.Bottom
        self.horizontalLabelAlignment = HorizontalLabelAlignment.Center
        self.showTitle = True
        self.fontFamily = "Arial"
        self.ports = {}
        self.flipHorizontal = False
        self.flipVertical = False
        self.rotation = 0
        self.textOffset = (0, 20)

    def updatePorts(self):
        self.ports = {}
        return

    def __getitem__(self, key):
        if key in self.ports:
            return self.ports[key]
        else:
            raise KeyError(f"UnitOperation {self.id} does not have a port named {key}")

    def flip(self, axis="horizontal"):
        if axis.lower() == "horizontal":
            self.flipHorizontal = True
            for p in self.ports.values():
                p.relativePosition = (
                    1 - (p.relativePosition[0]),
                    p.relativePosition[1],
                )
                p.normal = (p.normal[0] * -1, p.normal[1])
        if axis.lower() == "vertical":
            self.flipVertical = True
            for p in self.ports.values():
                p.relativePosition = (
                    (p.relativePosition[0]),
                    1 - p.relativePosition[1],
                )
                p.normal = (p.normal[0], p.normal[1] * -1)

        return

    def getNormalLength(self):
        a = radians(self.rotation)
        return 20 * sin(a)

    def rotate(self, angle):
        self.rotation = angle
        for p in self.ports.values():
            x = p.relativePosition[0] * self.size[0]
            y = p.relativePosition[1] * self.size[1]
            nx = p.normal[0]
            ny = p.normal[1]

            cx = 0.5 * self.size[0]
            cy = 0.5 * self.size[1]
            a = radians(angle)
            p.relativePosition = (
                (x * cos(a) - y * sin(a) - cx * cos(a) + cy * sin(a) + cx)
                / self.size[0],
                (x * sin(a) + y * cos(a) - cx * sin(a) - cy * cos(a) + cy)
                / self.size[1],
            )
            p.normal = (nx * cos(a) - ny * sin(a), nx * sin(a) + ny * cos(a))

    def intersectsPoint(self, point):
        test_x = (
            point[0] >= self.position[0] and point[0] <= self.position[0] + self.size[0]
        )
        test_y = (
            point[1] >= self.position[1] and point[1] <= self.position[1] + self.size[1]
        )
        return test_x and test_y

    def draw(self, ctx):

        if self.drawBoundingBox:
            ctx.rectangle(
                [
                    (self.position[0], self.position[1]),
                    (self.position[0] + self.size[0], self.position[1] + self.size[1]),
                ],
                fillColor=None,
                lineColor=(255, 0, 0, 255),
                lineSize=1,
            )

        return

    def setTextAnchor(self, horizontal, vertical, offset=None):

        if offset != None:
            self.textOffset = offset
        self.horizontalLabelAlignment = horizontal
        self.verticalLabelAlignment = vertical
        return

    def getTextAnchor(self):

        x = 0
        y = 0
        align = "middle"
        if self.horizontalLabelAlignment == HorizontalLabelAlignment.Center:
            x = self.position[0] + self.size[0] / 2
        if self.horizontalLabelAlignment == HorizontalLabelAlignment.LeftOuter:
            x = self.position[0]
            align = "end"
        if self.horizontalLabelAlignment == HorizontalLabelAlignment.Left:
            x = self.position[0]
            align = "start"
        if self.horizontalLabelAlignment == HorizontalLabelAlignment.RightOuter:
            x = self.position[0] + self.size[0]
            align = "start"
        if self.horizontalLabelAlignment == HorizontalLabelAlignment.Right:
            x = self.position[0] + self.size[0]
            align = "end"

        if self.verticalLabelAlignment == VerticalLabelAlignment.Center:
            y = self.position[1] + self.size[1] / 2
        elif self.verticalLabelAlignment == VerticalLabelAlignment.Bottom:
            y = self.position[1] + self.size[1]
        elif self.verticalLabelAlignment == VerticalLabelAlignment.Top:
            y = self.position[1]

        anchor = (x + self.textOffset[0], y + self.textOffset[1])

        return anchor, align

    def drawTextLayer(self, ctx):
        # for p in self.ports.values():
        #    p.draw(ctx)
        if self.showTitle:
            insert, align = self.getTextAnchor()
            ctx.text(
                insert,
                text=self.id,
                fontFamily=self.fontFamily,
                textColor=self.textColor,
                textAnchor=align,
            )
        return