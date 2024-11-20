import pygame


from figures import Figure #, Curve
from tools import Point
from typing import Callable, Dict


class RenderManager:
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
        if figure.name == 'line':
            pygame.draw.line(self.screen, pygame.Color(255, 255, 255), self.transform(figure.point1), self.transform(figure.point2))
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
    def __init__(self, render_manager: RenderManager, list_figures: list[Figure]) -> None:
        pygame.init()
        self.render_manager: RenderManager = render_manager
        self.list_figures: list[Figure] = list_figures

    def run(self) -> None:
        running: bool = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for figure in self.list_figures:
                self.render_manager.render(figure)
            pygame.display.update()
        pygame.quit()
        exit()

