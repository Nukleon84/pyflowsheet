import svgwrite
from .foreignObject import ForeignObject


class SvgContext(object):
    def __init__(self, filename, backgroundColor=None):
        self.dwg = svgwrite.Drawing(filename, profile="full")
        self.g = None
        self.gstack = []
        self.bounds = [1e6, 1e6, 200, 200]

        if backgroundColor != None:
            self.dwg.attribs["style"] = f"background-color:rgb{backgroundColor[0:3]}"

    def _updateBounds(self, rect):
        x1 = rect[0][0] - 40
        x2 = rect[1][0] + 40
        y1 = rect[0][1] - 40
        y2 = rect[1][1] + 40

        if x1 < self.bounds[0]:
            self.bounds[0] = x1
        if x2 > self.bounds[2]:
            self.bounds[2] = x2
        if y1 < self.bounds[1]:
            self.bounds[1] = y1
        if y2 > self.bounds[3]:
            self.bounds[3] = y2

    def rectangle(self, rect, fillColor, lineColor, lineSize):
        self._updateBounds(rect)
        if fillColor == None:
            self.g.add(
                self.dwg.rect(
                    insert=rect[0],
                    size=(f"{rect[1][0]-rect[0][0]}", f"{rect[1][1]-rect[0][1]}"),
                    fill_opacity="0",
                    stroke=f"rgb{lineColor[0:3]}",
                    stroke_width=lineSize,
                )
            )
        else:
            self.g.add(
                self.dwg.rect(
                    insert=rect[0],
                    size=(f"{rect[1][0]-rect[0][0]}", f"{rect[1][1]-rect[0][1]}"),
                    fill=f"rgb{fillColor[0:3]}",
                    stroke=f"rgb{lineColor[0:3]}",
                    stroke_width=lineSize,
                )
            )
        return

    def circle(self, rect, fillColor, lineColor, lineSize):
        self._updateBounds(rect)
        center = ((rect[0][0] + rect[1][0]) / 2, (rect[0][1] + rect[1][1]) / 2)
        r = (rect[1][0] - rect[0][0]) / 2
        if fillColor == None:
            self.g.add(
                self.dwg.circle(
                    center=center,
                    r=r,
                    fill_opacity="0",
                    stroke=f"rgb{lineColor[0:3]}",
                    stroke_width=lineSize,
                )
            )
        else:
            self.g.add(
                self.dwg.circle(
                    center=center,
                    r=r,
                    fill=f"rgb{fillColor[0:3]}",
                    stroke=f"rgb{lineColor[0:3]}",
                    stroke_width=lineSize,
                )
            )
        return

    def text(
        self, insert, text, fontFamily, textColor, fontSize=12, textAnchor="middle"
    ):
        self._updateBounds([insert, (insert[0] + 40, insert[1] + 20)])
        self.g.add(
            self.dwg.text(
                text,
                insert=insert,
                fill=f"rgb{textColor[0:3]}",
                font_family=fontFamily,
                text_anchor=textAnchor,
                font_size=fontSize,
            )
        )
        return

    def line(self, start, end, lineColor, lineSize):
        self._updateBounds([start, end])

        self.g.add(
            self.dwg.line(
                start=start,
                end=end,
                stroke=f"rgb{lineColor[0:3]}",
                stroke_width=lineSize,
            )
        )
        return

    def path(self, points, fillColor, lineColor, lineSize, close=False, dashArray=None):

        minx = min([(p[0]) for p in points])
        maxx = max([(p[0]) for p in points])
        miny = min([(p[1]) for p in points])
        maxy = max([(p[1]) for p in points])

        self._updateBounds([(minx, miny), (maxx, maxy)])

        path = svgwrite.path.Path(
            stroke=f"rgb{lineColor[0:3]}",
            stroke_width=lineSize,
        )
        if fillColor != None:
            path.attribs["fill"] = f"rgb{fillColor[0:3]}"
        else:
            path.attribs["fill"] = f"none"

        if dashArray != None:
            path.attribs["stroke-dasharray"] = dashArray

        path.push(f"M {points[0][0]} {points[0][1]} ")

        for p in points[1:]:
            path.push(f"L {p[0]} {p[1]} ")

        if close:
            path.push(f"Z")

        self.g.add(path)
        return

    def chord(self, rect, start, end, fillColor, lineColor, lineSize):
        self._updateBounds(rect)
        p = svgwrite.path.Path(
            fill=f"rgb{fillColor[0:3]}",
            stroke=f"rgb{lineColor[0:3]}",
            stroke_width=lineSize,
        )
        center = ((rect[0][0] + rect[1][0]) / 2, (rect[0][1] + rect[1][1]) / 2)
        rh = (rect[1][0] - rect[0][0]) / 2
        rv = (rect[1][1] - rect[0][1]) / 2

        if start == 180 and end == 360:
            start = (center[0] - rh, center[1])
            end = (center[0] + rh, center[1])

        if start == 90 and end == 270:
            start = (center[0], center[1] + rv)
            end = (center[0], center[1] - rv)

        if start == 270 and end == 90:
            start = (center[0], center[1] - rv)
            end = (center[0], center[1] + rv)

        if start == 0 and end == 180:
            start = (center[0] + rh, center[1])
            end = (center[0] - rh, center[1])

        p.push(f"M {center[0]} {center[1]} ")
        p.push(f"L {start[0]} {start[1]} ")
        p.push_arc(end, 0, (rh, rv), True, "+", True)
        p.push(f"Z")
        self.g.add(p)
        return

    def startGroup(self, id):
        if self.g != None:
            self.gstack.append(self.g)

        self.g = self.dwg.g(id=id)

    def startTransformedGroup(self, element):
        if self.g != None:
            self.gstack.append(self.g)

        self.g = self.dwg.g(id=element.id + "T")

        if element.flipHorizontal:
            self.g.attribs[
                "transform"
            ] = f"translate({element.position[0]+element.size[0]/2},0) scale(-1,1) translate({-(element.position[0]+element.size[0]/2)},0)"
        if element.flipVertical:
            self.g.attribs[
                "transform"
            ] = f"translate(0,{element.position[1]+element.size[1]/2}) scale(1,-1) translate(0,{-(element.position[1]+element.size[1]/2)})"

        if element.rotation != 0:
            self.g.attribs[
                "transform"
            ] = f"rotate({element.rotation},{element.position[0]+element.size[0]/2},{element.position[1]+element.size[1]/2} ) "
        return

    def endGroup(self):
        self.dwg.add(self.g)
        self.g = None
        if len(self.gstack) > 0:
            self.g = self.gstack.pop()
        return

    def html(self, html, position, size):
        html = "<body width='100%'>" + html + "</body>"
        e = ForeignObject(
            html,
            x=f"{position[0]}",
            y=f"{position[1]}",
            width=f"{size[0]}",
            height=f"{size[1]}",
        )
        e.translate(0.2 * position[0], 0.2 * position[1])
        e.scale(0.8)

        self.g.add(e)
        return

    def image(self, image, position, size):

        self.g.add(self.dwg.image(href=image, insert=position, size=size))
        return

    def render(self, width=None, height=None, scale=1, saveFile=True):

        if width == None:
            width = self.bounds[2] - self.bounds[0]
        if height == None:
            height = self.bounds[3] - self.bounds[1]

        width = width * scale
        height = height * scale

        self.dwg.attribs["width"] = f"{width}px"
        self.dwg.attribs["height"] = f"{height}px"

        self.dwg.viewbox(
            self.bounds[0],
            self.bounds[1],
            self.bounds[2] - self.bounds[0],
            self.bounds[3] - self.bounds[1],
        )

        if saveFile:
            self.dwg.save()

        return self.dwg.tostring()
