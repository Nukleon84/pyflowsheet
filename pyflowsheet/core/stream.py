from .pathfinder import Pathfinder, rectifyPath, compressPath


class Stream(object):
    def __init__(self, id, fromPort, toPort):
        self.id = id
        self.lineColor = (0, 0, 0, 255)
        self.textColor = (0, 0, 0, 255)
        self.lineSize = 2
        self.fromPort = fromPort
        self.toPort = toPort
        self.showTitle = True
        self.fontFamily = "Arial"
        self.dashArray = None
        self.manualRouting = []
        self.showPoints = False
        self.labelOffset = (0, 10)

    def draw(self, ctx, grid, minx, miny):

        if len(self.manualRouting) == 0:
            points, startAnchor = self._calculateAutoRoute(minx, miny, grid)
        else:
            points = []
            points.append(self.fromPort.get_position())

            for step in self.manualRouting:
                p = (points[-1][0] + step[0], points[-1][1] + step[1])
                points.append(p)

            points.append(self.toPort.get_position())
            startAnchor = points[0]

        ctx.path(
            points, None, self.lineColor, self.lineSize, False, self.dashArray, True
        )

        if self.showPoints:
            for p in points:
                ctx.circle(
                    [(p[0] - 2, p[1] - 2), (p[0] + 2, p[1] + 2)],
                    None,
                    (64, 64, 64, 255),
                    1,
                )

        textAnchor = (
            startAnchor[0] + self.labelOffset[0],
            startAnchor[1] + self.labelOffset[1],
        )
        ctx.text(
            textAnchor,
            text=self.id,
            fontFamily=self.fontFamily,
            textColor=self.textColor,
            fontSize="10",
        )

        grid.cleanup()

        return

    def _calculateAutoRoute(self, minx, miny, grid):
        normalLength = 10
        points = []
        gridsize = 10
        startAnchor = (
            self.fromPort.get_position()[0] + self.fromPort.normal[0] * normalLength,
            self.fromPort.get_position()[1] + self.fromPort.normal[1] * normalLength,
        )
        endAnchor = (
            self.toPort.get_position()[0] + self.toPort.normal[0] * normalLength,
            self.toPort.get_position()[1] + self.toPort.normal[1] * normalLength,
        )

        startAnchor2 = (
            self.fromPort.get_position()[0],
            self.fromPort.get_position()[1],
        )
        endAnchor2 = (
            self.toPort.get_position()[0],
            self.toPort.get_position()[1],
        )

        startAnchor = (
            round(startAnchor[0] / gridsize) * gridsize,
            round(startAnchor[1] / gridsize) * gridsize,
        )
        endAnchor = (
            round(endAnchor[0] / gridsize) * gridsize,
            round(endAnchor[1] / gridsize) * gridsize,
        )

        startAnchor2 = (
            round(startAnchor2[0] / gridsize) * gridsize,
            round(startAnchor2[1] / gridsize) * gridsize,
        )
        endAnchor2 = (
            round(endAnchor2[0] / gridsize) * gridsize,
            round(endAnchor2[1] / gridsize) * gridsize,
        )
        sx = round((startAnchor[0] - minx) / gridsize)
        sy = round((startAnchor[1] - miny) / gridsize)

        ex = round((endAnchor[0] - minx) / gridsize)
        ey = round((endAnchor[1] - miny) / gridsize)

        scx = round((startAnchor2[0] - minx) / gridsize)
        scy = round((startAnchor2[1] - miny) / gridsize)

        ecx = round((endAnchor2[0] - minx) / gridsize)
        ecy = round((endAnchor2[1] - miny) / gridsize)

        start = grid.node(scx, scy)
        end = grid.node(ecx, ecy)

        grid.node(sx, sy).walkable = True
        grid.node(ex, ey).walkable = True
        grid.node(scx, scy).walkable = True
        grid.node(ecx, ecy).walkable = True

        finder = Pathfinder()
        path, _ = finder.find_path(start, end, grid)

        w = 10

        for step in path:
            grid.node(step[0], step[1]).weight += w

        path = compressPath(path)

        points.append(self.fromPort.get_position())
        for step in path:
            p = (step[0] * gridsize + minx, step[1] * gridsize + miny)
            points.append(p)

        realendpoint = self.toPort.get_position()
        if realendpoint[0] != points[-1][0] or realendpoint[1] != points[-1][1]:
            points.append(realendpoint)
        return points, startAnchor
