import svgwrite


class ForeignObject(
    svgwrite.base.BaseElement,
    svgwrite.mixins.Transform,
    svgwrite.container.Presentation,
):
    elementname = "foreignObject"

    def __init__(self, obj, **extra):
        super().__init__(**extra)
        self.obj = obj

    def get_xml(self):
        xml = super().get_xml()
        xml.append(svgwrite.etree.etree.fromstring(self.obj))
        return xml
