from .unitoperation import UnitOperation
from .port import Port

import matplotlib.pyplot as plt
import base64
from io import BytesIO

plt.ioff()


class Table(UnitOperation):
    def __init__(
        self,
        id: str,
        name: str,
        data,
        position=(0, 0),
        size=(40, 20),
        figsize=(5, 5),
        description: str = "",
    ):
        super().__init__(id, name, position=position, size=size)
        self.data = data
        self.drawBoundingBox = False
        self.figsize = figsize
        return

    def draw(self, ctx):

        # html = self.data.to_html()
        # ctx.html(html, self.position, self.size)

        cell_text = []
        for row in range(len(self.data)):
            cell_text.append(self.data.iloc[row])
        plt.figure(figsize=self.figsize)

        plt.table(
            cellText=cell_text,
            colLabels=self.data.columns,
            loc="center",
            bbox=[0, 0, 1, 1],
        )
        plt.axis("off")

        fig = plt.gcf()
        fig.tight_layout()
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format="png")
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