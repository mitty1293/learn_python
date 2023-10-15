from decorator.interface import DrawingInterface, Point
from thirdpirty import VendorGraphicsInterface


class VendorGraphicsDrawingAdapter(DrawingInterface):
    def __init__(self, target: VendorGraphicsInterface):
        self.target = target
        self.current = None

    def start_at(self, p: Point):
        self.current = p

    def line_to(self, p: Point):
        if self.current is None:
            raise LogicException()
        p0 = self.current
        self.target.line(p0.x, p0.y, p.x, p.y)
        self.current = p
