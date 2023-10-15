from interface import DrawingInterface, Point


class DecorativeDrawing(DrawingInterface):
    def __init__(self, target: DrawingInterface):
        self.target = target

    def start_at(self, p: Point):
        self.target.start_at(p)

    def line_to(self, p: Point):
        self.target.line_to(p)

    def rectangle(self, top_left: Point, bottom_right: Point):
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)
        self.start_at(top_left)
        self.line_to(top_right)
        self.line_to(bottom_right)
        self.line_to(bottom_left)
        self.line_to(top_left)

    def triangle(self, p0: Point, p1: Point, p2: Point):
        self.start_at(p0)
        self.line_to(p1)
        self.line_to(p2)
        self.line_to(p0)

    # その他の図形メソッドなど
