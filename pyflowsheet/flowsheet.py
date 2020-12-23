from .stream import Stream
from pathfinding.core.grid import Grid
from .textelement import TextElement


class Flowsheet(object):
    def __init__(self, id: str, name: str, description: str = ""):
        """Generates a new Flowsheet Object. The Flowsheet object represent a Process Flow Diagram (PFD). A Flowsheet
        is made up of unit operations, streams and annotations.

        Args:
            id (str): Short identifier of the flowsheet
            name (str): A human readable, longer name
            description (str, optional): A text that describes the process task of the flowsheet. Defaults to "".
        """
        self.id = id
        self.name = name
        self.description = description
        self.lineColor = (64, 64, 64, 255)
        self.fillColor = (255, 255, 255, 255)
        self.textColor = (0, 0, 0, 255)
        self.size = (512, 512)
        self.position = (0, 0)
        self.lineSize = 2
        self.unitOperations = {}
        self.annotations = []
        self.streams = {}
        self.showGrid = False

    def addAnnotations(self, elements):
        for e in elements:
            self.annotations.append(e)
        return

    def addUnits(self, units):
        """Add a list of units to the flowsheet in one go.

        Args:
            units (List[UnitOperation]): A list of UnitOperation objects
        """
        for u in units:
            self.unitOperations[u.id] = u
        return

    def connect(self, name, fromPort, toPort):
        """Connect two ports of two unit operations with a stream.

        Args:
            name (string): The identifier/name of the stream.
            fromPort (Port): The source port from which to route the stream
            toPort (Port): The destination port to which to route the stream
        """
        self.streams[name] = Stream(name, fromPort, toPort)
        return

    def _calcGrid(self):
        """Private helper function to rasterize the canvas and generate a course grid for pathfinding. This functions scans
        the entire canvas area and tests if a unit intersects the grid point. If any unit does so, the point is marked as
        "impassable" for the pathfinding algorithm.

        Returns:
            [2d-list]: The reachability matrix of the canvas area
            [int]    : The minimum x coordinate of the canvas (upper-left)
            [int]    : The minimum y coordinate of the canvas (upper-left)
        """
        minx = min([u.position[0] for u in self.unitOperations.values()])
        maxx = max([u.position[0] + u.size[0] for u in self.unitOperations.values()])
        miny = min([u.position[1] for u in self.unitOperations.values()])
        maxy = max([u.position[1] + u.size[1] for u in self.unitOperations.values()])

        gridsize = 10

        minx = int(minx / gridsize - 8) * gridsize
        miny = int(miny / gridsize - 8) * gridsize
        maxx = int(maxx / gridsize + 8) * gridsize
        maxy = int(maxy / gridsize + 8) * gridsize

        grid = []

        for y in range(miny, maxy, gridsize):
            row = []
            for x in range(minx, maxx, gridsize):
                intersectionFound = False

                for u in self.unitOperations.values():
                    if u.intersectsPoint((x, y)):
                        intersectionFound = True

                if intersectionFound:
                    row.append(0)
                else:
                    row.append(1)
            grid.append(row)

        return grid, minx, miny

    def _drawGrid(self, grid, ctx, minx, miny):
        ctx.startGroup("RoutingGrid")

        for y in range(grid.height):
            for x in range(grid.width):
                sx = minx + x * 10
                sy = miny + y * 10
                if not grid.node(x, y).walkable:
                    ctx.circle(
                        [(sx - 5, sy - 5), (sx + 5, sy + 5)],
                        (0, 0, 0, 255),
                        (0, 0, 0, 255),
                        1,
                    )
                else:
                    w = 255 - 10 * grid.node(x, y).weight
                    w = max(w, 0)
                    ctx.circle(
                        [(sx - 5, sy - 5), (sx + 5, sy + 5)],
                        (w, w, w, 255),
                        (0, 0, 0, 255),
                        1,
                    )

        ctx.endGroup()

        return
        # ctx.circle(
        #     [(x - 5, y - 5), (x + 5, y + 5)],
        #     (64, 64, 64, 255),
        #     (64, 64, 64, 255),
        #     1,
        # )
        # ctx.circle(
        #     [(x - 5, y - 5), (x + 5, y + 5)], None, (64, 64, 64, 255), 1
        # )

    def callout(self, text, position):
        text = TextElement(text, position)
        self.annotations.append(text)
        return

    def draw(self, ctx):
        """Draws the process flow diagram with the help of the context passed as an argument.
        This function has 3 stages. In the first stage, the reachability map of the diagram is calculated, which is used in
        the second stage to route the streams using Dykstra's algorithm. In the third stage, the unit operations are drawn.

        The unit operation draw loop has two stages. In the first stage the icon is drawn with transformations applied.
        In the second stage the text layer is drawn without any transformations (i.e. rotation) applied.

        Args:
            ctx ([type]): A drawing context that provides an abstraction for the primitive drawing functions.

        Returns:
            [type]: The same context as was passed in
        """

        matrix, minx, miny = self._calcGrid()
        grid = Grid(matrix=matrix)

        for s in self.streams.values():
            ctx.startGroup(s.id)
            s.draw(ctx, grid, minx, miny)
            ctx.endGroup()

        if self.showGrid:
            self._drawGrid(grid, ctx, minx, miny)

        # print(grid.grid_str(show_weight=True))
        for u in self.unitOperations.values():
            ctx.startGroup(u.id)
            ctx.startTransformedGroup(u)
            u.draw(ctx)
            ctx.endGroup()
            u.drawTextLayer(ctx)
            ctx.endGroup()

        for e in self.annotations:
            ctx.startGroup(e.id)
            e.draw(ctx)
            e.drawTextLayer(ctx)
            ctx.endGroup()

        return ctx