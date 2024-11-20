from tools import Point
class Figure:
    @property
    def name(self):
        return self._name

    def get_args(self) -> tuple[Point|float|str]:
        raise NotImplemented

class Line(Figure):
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1: Point = point1
        self.point2: Point = point2
        self._name: str = 'line'

    def get_args(self) -> tuple[Point, Point|float|str]:
        return self.point1, self.point2


class Circle(Figure):
    def __init__(self, center:Point, r: float) -> None:
        self.center: Point = center
        self.r: float = r
        self._name: str = 'circle'

    def get_args(self) -> tuple[Point, Point|float|str]:
        return self.center, self.r


class Text(Figure):
    def __init__(self, point: Point, text: str):
        self._name: str = 'text'
        self.text: str = text
        self.point: Point = point

    def get_args(self) -> tuple[Point, Point|float|str]:
        return self.point, self.text