from PIL import Image, ImageDraw


class BitmapContext(object):
    def __init__(self, size):
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