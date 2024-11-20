import math
from figures import Figure, Circle, Line, Text #, Curve
from graphs import Graph
from tools import Point



class Constructor:
    """
    Преобразование графа в объекты отображения.
    """

    def __init__(self, graph: Graph, radi: int, radi_t: int, r: int) -> None:
        self.graph: Graph = graph
        self.radi: int = radi
        self.radi_t: int = radi_t
        self.r: int = r


    def get_coordinates(self, n: int, radi: int) -> list[Point]:
        acordinat: list[Point] = []
        l: float = math.pi * 2 / n
        for x in range(n):
            acordinat.append(Point(radi * math.cos(x * l), radi * math.sin(x * l)))
        return acordinat



    
    def get_points(self, coord: list[Point]) -> dict[int, Point]:
        ponts: dict[int, Point] = {}
        for i, x in enumerate(self.graph.vehicles):
            ponts[x] = coord[i]
        return ponts

    def get_figures(self) -> list[Figure]:
        res: list[Figure] = []
        n: int = len(self.graph)
        coord: list[Point] = self.get_coordinates(n, self.radi)
        coord_text: list[Point] = self.get_coordinates(n, self.radi_t)
        d: dict[int, Point] = self.get_points(coord)
        d_text: dict[int, Point] = self.get_points(coord_text)
        for v in self.graph.vehicles:
            res.append(Circle(d[v], self.r * 0.5))
            res.append(Text(d_text[v], str(v)))
            for v2 in self.graph.get_adjacents(v):
                # if v == v2:
                #     res.append(Curve(d[v] * 1.090, self.r * 2))
                # else:
                res.append(Line(d[v], d[v2]))
        return res
