from .unitoperation import UnitOperation
from .port import Port

import importlib.util

package_name = "matplotlib"
spec = importlib.util.find_spec(package_name)

if spec is None:
    Warning(
        "Matplotlib is not installed. You cannot render tables. Please install matplotlib first"
    )
    PYFLOWSHEET_MATPLOTLIB_MISSING = True
else:
    import matplotlib.pyplot as plt
    import base64
    from io import BytesIO

    plt.ioff()
    PYFLOWSHEET_MATPLOTLIB_MISSING = False


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
        cell_text = []
        if not PYFLOWSHEET_MATPLOTLIB_MISSING:
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

            htmlString = "data:image/png;base64,{}".format(encoded)
            ctx.image(htmlString, self.position, self.size)
        else:
            start = (self.position[0], self.position[1])
            end = (
                self.position[0] + self.size[0],
                self.position[1] + self.size[1],
            )
            ctx.line(start, end, (255, 0, 0), self.lineSize)

            start = (self.position[0] + self.size[0], self.position[1])
            end = (self.position[0], self.position[1] + self.size[1])
            ctx.line(start, end, (255, 0, 0), self.lineSize)

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