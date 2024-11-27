from tools import Point


class Figure:
    @property
    def name(self):
        return self._name

    def get_args(self) -> tuple[Point|float|str]:
        raise NotImplementedError()


class Line(Figure):
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self._name:str = "line"

    def get_args(self):
        return self.p1, self.p2


class Circle(Figure):
    def __init__(self, center:Point, r: float):
        self.center: Point = center
        self.r: float = r
        self._name: str ="circle"

    def get_args(self):
        return self.center, self.r


class Text(Figure):
    def __init__(self, text: str, p: Point):
        self.text: str = text
        self.p: Point = p
        self._name: str = "text"

    def get_args(self):
        return self.text, self.p