from ..core import UnitOperation
from ..core.enums import HorizontalLabelAlignment, VerticalLabelAlignment


class TextElement(UnitOperation):
    def __init__(self, text, position=(0, 0)):
        super().__init__("text", "text", position=position, size=(20, 20))
        self.text = text
        self.drawBoundingBox = False
        self.showTitle = False
        self.fontFamily = "Consolas"
        return

    def draw(self, ctx):
        # html = self.data.to_html()
        # ctx.html(html, self.position, self.size)

        ctx.text(
            self.position,
            text=self.text,
            fontFamily=self.fontFamily,
            textColor=self.textColor,
            textAnchor="start",
        )
        # super().draw(ctx)

        return