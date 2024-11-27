import pygame

from figures import Figure
from tools import Point


class RenderManager:
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font_style = pygame.font.SysFont(None, 50)
        self.s = 60
        self.dx = 300
        self.dy = 300

    def fill(self):
        self.screen.fill(RenderManager.WHITE)

    def update(self):
        pygame.display.update()

    def _scale(self, number: float) -> float:
        """
        Масштабирование
        :param coord:
        :return:
        """
        return number * self.s

    def _move_x(self, coord: float) -> float:
        """
        Сдвиг по x
        :param coord:
        :return:
        """
        coord += self.dx
        return coord

    def _move_y(self, coord: float) -> float:
        """
        Сдвиг по y
        :param coord:
        :return:
        """
        coord += self.dy
        return coord

    def tranform(self, a: Point|float) -> tuple[float, float]|float:
        if isinstance(a, Point):
            x,y = a.to_tuple()
            return self._move_x(self._scale(x)), self._move_y(self._scale(y))
        else:
            return self._scale(a)

    def render(self, figure: Figure):
        match figure.name:
            case "text":
                msg = self.font_style.render(figure.get_args()[0], True, RenderManager.BLACK)
                self.screen.blit(msg, self.tranform(figure.get_args()[1]))
            case "line":
                pygame.draw.line(self.screen,
                                 RenderManager.BLACK,
                                 self.tranform(figure.get_args()[0]),
                                 self.tranform(figure.get_args()[1]))
            case "circle":
                pygame.draw.circle(self.screen,
                                 RenderManager.BLACK,
                                 self.tranform(figure.get_args()[0]),
                                 figure.get_args()[1])

        # self.func[figure.name](self.surface, self.color, *map(self.transform, figure.get_args()))


class GameManager:
    FPS = 30
    def __init__(self, RM: type[RenderManager], list_figures: list[Figure]):
        pygame.init()
        self.render_manager = RM()
        self.clock = pygame.time.Clock()
        self.list_figures = list_figures

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.render_manager.fill()
            for figure in self.list_figures:
                self.render_manager.render(figure)

            self.render_manager.update()
            self.clock.tick(GameManager.FPS)
        pygame.quit()
