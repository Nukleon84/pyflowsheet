class Port(object):
    def __init__(self, name, parent, rel_pos, normal, intent="in"):
        self.name = name
        self.relativePosition = rel_pos
        self.normal = normal
        self.size = (6, 6)
        self.fillColor = None
        self.lineColor = (0, 0, 255, 255)
        self.lineSize = 1
        self.parent = parent
        self.intent = intent

    def get_position(self):

        base_x = (
            self.parent.position[0] + self.relativePosition[0] * self.parent.size[0]
        )
        base_y = (
            self.parent.position[1] + self.relativePosition[1] * self.parent.size[1]
        )
        return (base_x, base_y)

    def draw(self, ctx):

        base_x, base_y = self.get_position()

        ctx.circle(
            [
                (base_x - self.size[0] / 2, base_y - self.size[1] / 2),
                (base_x + self.size[0] / 2, base_y + self.size[1] / 2),
            ],
            self.fillColor,
            self.lineColor if self.intent == "in" else (255, 0, 0, 255),
            self.lineSize,
        )
