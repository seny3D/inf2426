import pygame

from figures import Figure
from tools import Point


class RenderManager:
    def __init__(self):
        ...

    def _scale(self, number: float) -> float:
        """
        Масштабирование
        :param coord:
        :return:
        """

    def _move_x(self, coord: float) -> float:
        """
        Сдвиг по x
        :param coord:
        :return:
        """

    def _move_y(self, coord: float) -> float:
        """
        Сдвиг по y
        :param coord:
        :return:
        """

    def tranform(self, a: Point|float) -> tuple[float, float]|float:
        if isinstance(a, Point):
            x,y = a.to_tuple()
            return self._move_x(self._scale(x)), self._move_y(self._scale(y))
        else:
            return self._scale(a)

    def render(self, figure: Figure):
        self.func[figure.name](self.surface, self.color, *map(self.transform, figure.get_args()))


class GameManager:
    def __init__(self, render_manager: RenderManager, list_figures: list[Figure]):
        ...

    def run(self):
        while True:
            ...
            for figure in self.list_figures:
                self.render_manager.render(figure)
            ...