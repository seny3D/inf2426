import random
from collections import deque
from typing import Self, Type

import pygame


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Self) -> None:
        self = self + other

    def intersection(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y


class Food(Point):
    ...

class Snake:
    def __init__(self, x: int, y: int):
        self.head: Point = Point(x, y)
        self.body: deque[Point] = deque()
        self.length: int = 1

    def _move(self, p: Point) -> None:
        self.head += p
        self.body.append(self.head)
        if len(self.body) > self.length:
            self.body.popleft()

    def up(self) -> None:
        self._move(Point(0, -1))

    def down(self) -> None:
        self._move(Point(0, 1))

    def left(self) -> None:
        self._move(Point(-1, 0))

    def right(self) -> None:
        self._move(Point(1, 0))

    def is_correct(self) -> bool:
        for el in self.body:
            if el == self.head:
                return False
        return True

    def eat(self):
        self.length += 1


class Event:
    UP: str = "up"
    DOWN: str = "down"
    LEFT: str = "left"
    RIGHT: str = "right"
    NOTHING: str = ""
    QUIT: str = "quit"

    def __init__(self, name):
        self.name: str = name


class EventManager:

    def get_event(self) -> Event:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Event(Event.QUIT)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return Event(Event.LEFT)
                elif event.key == pygame.K_RIGHT:
                    return Event(Event.RIGHT)
                elif event.key == pygame.K_UP:
                    return Event(Event.UP)
                elif event.key == pygame.K_DOWN:
                    return Event(Event.DOWN)
        return Event(Event.NOTHING)



class Game:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.snake:  Snake| None = self.init_snake()
        self.game_over: bool = False
        self.food: Food = self.generate_food()

    def inside_field(self, p: Point) -> bool:
        return p.x > self.width - 1 or p.x < 0 or p.y > self.height - 1 or p.y < 0

    def step(self, event: Event):
        self.do_event(event)
        self.game_over = not self.snake.is_correct() or \
                            not self.inside_field(self.snake.head)
        if self.snake.head.intersection(self.food):
            food = self.generate_food()
            self.snake.eat()


    def do_event(self, event):
        if event.name == Event.UP:
            self.snake.up()
        if event.name == Event.DOWN:
            self.snake.down()
        if event.name == Event.LEFT:
            self.snake.left()
        if event.name == Event.RIGHT:
            self.snake.right()

    def generate_food(self) -> Food:
        x: int = random.randint(0, self.width - 1)
        y: int = random.randint(0, self.height -1 )
        return Food(x, y)

    def init_snake(self) -> Snake:
        x: int = self.width // 2
        y: int = self.height // 2
        return Snake(x, y)

class Color:
    def __init__(self, r, g, b):
        self.r: int = r
        self.g: int = g
        self.b: int = b

class RenderManager:
    BLACK: Color = Color(0, 0, 0)
    WHITE: Color = Color(255, 255, 255)
    RED: Color = Color(255, 0, 0)
    GREEN: Color = Color(0, 255, 0)

    def __init__(self, block_size: int, game: Game):
        self.game = game
        self.block_size: int = block_size
        self.screen = pygame.display.set_mode((self.game.width * self.block_size, self.game.height * self.block_size))
        self.font_style = pygame.font.SysFont(None, 5 * self.block_size)

    def set_caption(self, caption: str):
        pygame.display.set_caption(caption)


class GameManager:
    def __init__(self, event_manager_class: Type[EventManager],
                 game: Game,
                 render_manager_class: Type[RenderManager],
                 fps: int,
                 caption: str):
        self.caption: str = caption
        self.fps: int = fps
        self.game: Game = game
        pygame.init()
        self.event_manager: EventManager = event_manager_class()
        self.render_manager: RenderManager = render_manager_class(block_size=10, game=self.game)
        self.render_manager.set_caption(self.caption)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            event: Event = self.manager_event.get_event()
            self.game.step(event)

            self.screen.fill(WHITE)

            if game_over:
                message("Вы проиграли", GREEN)
            # pygame.draw.rect(screen, RED, [x0, y0, snake_block, snake_block])
            draw_snake(snake_list)
            pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])

            pygame.display.update()

            self.clock.tick(self.fps)

        pygame.quit()
        quit()




if __name__ == "__main__":
    g: GameManager = GameManager(event_manager_class=EventManager,
                                 game=Game(80, 60),
                                 render_manager_class=RenderManager,
                                 fps=20,
                                 caption="Игра Змейка")
    g.run()