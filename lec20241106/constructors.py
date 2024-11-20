from figures import Figure, Circle, Line, Text
from graphs import Graph
from tools import Point


class Constructor:
    """
    Преобразование графа в объекты отображения.
    """
    def __init__(self, graph:Graph):
        ...

    def get_coordinates(self, n:int, r: float) -> list[Point]:
        """
        Возвращает спискок координат по количеству вершин на окружности радиуса r
        :param n:
        :return:
        """

    def get_points(self, coordinates: list[Point]) -> dict[int, Point]:
        """
        Возвращает словарь соответствия вершинам графа - координат
        :param coordinates:
        :return:
        """

    def get_figures(self) -> list[Figure]:
        res: list[Figure] = []
        n: int = len(self.graph)
        coordinates: list[Point] = self.get_coordinates(n, self.r)
        coordinates_text: list[Point] = self.get_coordinates(n, self.r_text)
        d: dict[int, Point] = self.get_points(coordinates)
        d_text: dict[int, Point] = self.get_points(coordinates_text)
        for v in self.graph.vertices:
            res.append(Circle(d[v], self.r_v))
            res.append(Text(str(v), d_text[v]))
            for v2 in self.graph.get_adjacents(v):
                res.append(Line(d[v], d[v2]))
        return res

