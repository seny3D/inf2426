import pygame

from constructors import Constructor
from figures import Figure #, Curve
from tools import Point
from typing import Callable, Dict, Tuple


class Color:
    def __init__(self, r, g, b) -> None:
        self.r: int = r
        self.g: int = g
        self.b: int = b
    def get(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)

class RenderManager:
    BACKGROUND_COLOR: Color = Color(0, 0, 0)
    def __init__(self) -> None:
        xcord: int = 80
        ycord: int = 60
        bsize: int = 10
        self.scalef: float = 10
        self.xmove: float = xcord * bsize // 2
        self.ymove: float = ycord * bsize // 2
        self.func: Dict[str, Callable[[tuple], None]] = {}
        self.screen: pygame.Surface = pygame.display.set_mode((xcord * bsize,
                                               ycord * bsize))


    def fill_background(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR.get())

    def _scale(self, number: float) -> float:
        # Масштабирование
        return self.scalef * number

    def _move_x(self, coord: float):
        # Свдиг по х
        return self.xmove + coord
    def _move_y(self, coord: float):
        # Сдвиг по y
        return self.ymove + coord


    def transform(self, a: Point|float) -> tuple[float, float]|float:
        if isinstance(a, Point):
            x: float
            y: float
            x, y = a.to_tuple()
            return self._move_x(self._scale(x)), self._move_y(self._scale(y))
        else:
            return self._scale(a)

    def render(self, figure: Figure) -> None:
        if figure.name == "circle":
            pygame.draw.circle(self.screen, pygame.Color(0, 0, 255), self.transform(figure.center), self.transform(figure.r))
            print(self.transform(figure.center))
        if figure.name == 'line':
            pygame.draw.aaline(self.screen, pygame.Color(255, 255, 255), self.transform(figure.point1), self.transform(figure.point2))
        # if figure.name == 'curve':
        #     pygame.draw.circle(self.screen, pygame.Color(255, 255, 255), self.transform(figure.center), self.transform(figure.r), 1)
        if figure.name == 'text':
            font_style: pygame.font.Font = pygame.font.SysFont(None, 5 * 10)
            mes: pygame.Surface = font_style.render(str(figure.text), True, pygame.Color(0, 255, 0))
            x: float
            y: float
            x, y = self.transform(figure.point)
            self.screen.blit(mes, (x - mes.get_width() // 2, y - mes.get_height() // 2))
class GameManager:
    def __init__(self, render_manager: RenderManager, constructors: Constructor) -> None:
        pygame.init()
        self.render_manager: RenderManager = render_manager
        self.constructors: Constructor = constructors
        self.render_manager.fill_background()

    def run(self) -> None:
        running: bool = True
        while running:
            self.render_manager.fill_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for figure in self.constructors.get_figures():
                self.render_manager.render(figure)
            pygame.display.update()
        pygame.quit()
        exit()

