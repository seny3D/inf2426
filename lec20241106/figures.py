from tools import Point


class Figure:
    @property
    def name(self):
        return self._name

    def get_args(self) -> tuple[Point|float|str]:
        raise NotImplementedError()


class Line(Figure):
    ...


class Circle(Figure):
    def __init__(self, center:Point, r: float):
        self.center: Point = center
        self.r: float = r
        self._name: str ="circle"

    def get_args(self):
        return self.center, self.r

class Text(Figure):
    ...