from typing import Self

class Vec():
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y


    def __add__(self, v: Self):
        return Vec(self.x + v.x, self.y + v.y)

    def __str__(self):
        return str((self.x, self.y))


    def __sub__(self, g: Self):
        return Vec(self.x - g.x, self.y - g.y)

    def __mul__(self, p: Self):
        return Vec(self.x * p.x, self.y * p.y)


if __name__ == '__main__':
    coord: Vec = Vec(5, 4)
    coord2: Vec = Vec(2,3)

    print('сумма ', coord + coord2)
    print('вычитание ', coord - coord2)
    print('умнож ', coord * coord2)