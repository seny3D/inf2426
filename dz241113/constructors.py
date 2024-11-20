import math
import random
from collections import defaultdict
from typing import Self
from figures import Figure, Circle, Line, Text #, Curve
from graphs import Graph
from tools import Point, Vec

class IConstructor:
    def get_figures(self) -> list[Figure]:
        raise NotImplementedError


class Constructor(IConstructor):
    """
    Преобразование графа в объекты отображения.
    """

    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.radi: int = 20
        self.radi_t: int = 25
        self.r: int = 1


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

class ConstructorGravity(IConstructor):
    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.r: float = 15
        self.coord: list[Point] = self.random_coord()
        self.gravity: float = 1000

    def random_coord(self) -> list[Point]:
        acordinat: list[Point] = []
        for x in range(len(self.graph)):
            acordinat.append(Point(random.uniform(-25, 25), random.uniform(-25, 25)))
        return acordinat

    def get_points(self, coord: list[Point]) -> dict[int, Point]:
        ponts: dict[int, Point] = {}
        for i, x in enumerate(self.graph.vehicles):
            ponts[x] = coord[i]
        return ponts


    def move(self, vec: Vec = Vec) -> Vec:
        lenghtvec: float = abs(math.sqrt(((vec.end.x - vec.first.x) ** 2) +
                                                       ((vec.end.y - vec.first.y) ** 2)))
        return vec * ((-(self.gravity / lenghtvec ** 2)) / lenghtvec)

    def shift(self) -> None:
        for x in range(len(self.coord)):
            self.coord[x] += Point(0.01, 0)

    def shiftvect(self) -> None:
        movevec: defaultdict[int, Vec] = defaultdict()
        for x in range(len(self.coord)):
            resvec: Vec = Vec()
            for i in range(len(self.coord)):
                if x == i:
                    continue
                curvec: Vec = self.move(Vec(self.coord[x], self.coord[i]))
                if resvec.first is not None and resvec.end is not None:
                    res = res + curvec
                else:
                    res = curvec
            movevec[x]: defaultdict[int, Vec] = res / (len(self.graph) + 1)

        for x in range(len(self.coord)):
            self.coord[x]: list[Point] = movevec[x].end

    def get_figures(self) -> list[Figure]:
        res: list[Figure] = []
        d: dict[int, Point] = self.get_points(self.coord)
        for v in self.graph.vehicles:
            res.append(Circle(d[v], self.r * 0.1))
            for v2 in self.graph.get_adjacents(v):
                res.append(Line(d[v], d[v2]))
        self.shiftvect()
        return res