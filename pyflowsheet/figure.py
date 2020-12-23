from .unitoperation import UnitOperation
from .port import Port

import base64
from io import BytesIO


class Figure(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        fig,
        position=(0, 0),
        size=(40, 20),
        description: str = "",
    ):
        super().__init__(id, name, position=position, size=size)
        self.fig = fig
        self.drawBoundingBox = False

        return

    def draw(self, ctx):

        tmpfile = BytesIO()
        self.fig.savefig(tmpfile, format="png")
        encoded = base64.b64encode(tmpfile.getvalue()).decode("utf-8")

        data = "data:image/png;base64,{}".format(encoded)

        # html = self.data.to_html()
        # ctx.html(html, self.position, self.size)
        ctx.image(data, self.position, self.size)
        ctx.rectangle(
            [
                self.position,
                (self.position[0] + self.size[0], self.position[1] + self.size[1]),
            ],
            None,
            self.lineColor,
            self.lineSize,
        )

        super().draw(ctx)

        return