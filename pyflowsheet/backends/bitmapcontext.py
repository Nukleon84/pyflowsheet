import importlib.util

package_name = "pillow"
spec = importlib.util.find_spec(package_name)

if spec is None:
    Warning("Pillow is not installed. You cannot render to the bitmap context!")
    PYFLOWSHEET_PILLOW_MISSING = True
else:
    from PIL import Image, ImageDraw

    PYFLOWSHEET_PILLOW_MISSING = False


class BitmapContext(object):
    def __init__(self, size):

        if PYFLOWSHEET_PILLOW_MISSING:
            Warning("Pillow is not installed. You cannot render to the bitmap context!")
        self.img = Image.new("RGBA", size, (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)

    def rectangle(self, rect, fillColor, lineColor, lineSize):
        self.draw.rectangle(rect, fillColor, lineColor, lineSize)
        return

    def chord(self, rect, start, end, fillColor, lineColor, lineSize):
        self.draw.chord(rect, start, end, fillColor, lineColor, width=lineSize)
        return

    def circle(self, rect, fillColor, lineColor, lineSize):
        return

    def text(self, x, y, text, fontFamily, textColor):
        return

    def render(self):
        return self.img