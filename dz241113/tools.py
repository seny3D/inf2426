from typing import Self
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other) -> Self:
        return self.x == other.x and self.y == other.y

    def __truediv__(self, other: Self) -> Self:
        return Point(self.x / other, self.y / other)

    def __mul__(self, other) -> Self:
        return Point(self.x * other, self.y * other)

    def to_tuple(self) -> tuple[float, float]:
       return self.x, self.y

class Vec:
    def __init__(self, first: Point = None, end: Point = None) -> None:
        self.first: Point = first
        self.end: Point = end

    def __add__(self, other: Self) -> Self: # сложение векторов
        return Vec(self.first, Point(self.end.x - self.first.x, self.end.y - self.first.y)
                   + Point(other.end.x - other.first.x, other.end.y - other.first.y))

    def __mul__(self, other: float) -> Self: # умножение векторов
        return Vec(self.first, ((self.end - self.first) * other) + self.first)

    def __truediv__(self, other: Self) -> Self: # деление
        return Vec(self.first, ((self.end - self.first) / other) + self.first)

