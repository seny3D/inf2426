class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    def to_tuple(self) -> tuple[float, float]:
       return self.x, self.y