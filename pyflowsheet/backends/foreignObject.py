import svgwrite


class ForeignObject(
    svgwrite.base.BaseElement,
    svgwrite.mixins.Transform,
    svgwrite.container.Presentation,
):
    """Create an instance of the ForeignObject class. This class describes an add-on to svgwrite and allows arbitrary HTML code to be embedded in SVG drawings.

    Args:
        svgwrite ([type]): [description]
        svgwrite ([type]): [description]
        svgwrite ([type]): [description]

    Returns:
        [type]: [description]
    """

    elementname = "foreignObject"

    def __init__(self, obj, **extra):
        super().__init__(**extra)
        self.obj = obj

    def get_xml(self):
        xml = super().get_xml()
        xml.append(svgwrite.etree.etree.fromstring(self.obj))
        return xml
