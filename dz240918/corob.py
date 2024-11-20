class Corob:
    def __init__(self, x: float, y: float):
        # Учитываем ширину краев коробки
        self.x: float = x # длина, края учитываются далее
        self.y: float = y # ширина, края учитываются далее

    def __lt__(self, other) -> bool:
        # проверяем размеры коробок, ширину учитывали ранее
        return (((self.x < other.x) and (self.y < other.y)) or
                ((self.x < other.y) and (self.y < other.x)))

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def __repr__(self) -> str:
        return f"Corob({self.x}, {self.y})"
