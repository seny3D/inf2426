from typing import Self
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __eq__(self, other) -> Self:
        return self.x == other.x and self.y == other.y

    def __mul__(self, other) -> Self:
        return Point(self.x * other, self.y * other)

    def __add__(self, other: Self) -> None:
        self.x += other.x
        self.y += other.y

    def to_tuple(self) -> tuple[float, float]:
       return self.x, self.y