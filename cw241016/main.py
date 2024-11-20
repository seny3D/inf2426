import random
from collections import deque
from typing import Self, Type

#
import pygame


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Self) -> Self:
        return self + other

    def intersection(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y


class Food(Point):
    ...


class Snake:
    def __init__(self, x: int, y: int):
        self.head: Point = Point(x, y)
        self.body: deque[Point] = deque()
        self.length: int = 1
        self.bias: Point = Point(0, 0)

    def move(self) -> None:
        self.head += self.bias
        self.body.append(self.head)
        if len(self.body) > self.length:
            self.body.popleft()

    def up(self) -> None:
        self.bias = Point(0, -1)

    def down(self) -> None:
        self.bias = Point(0, 1)

    def left(self) -> None:
        self.bias = Point(-1, 0)

    def right(self) -> None:
        self.bias = Point(1, 0)

    def is_correct(self) -> bool:
        for el in list(self.body)[:-1]:
            if el.intersection(self.head):
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
    PAUSE: str = 'pause'

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
                self.game.pause = False
                return Event(Event.PAUSE)
        return Event(Event.NOTHING)


class Game:
    GAME_OVER_MESSAGE: str = "Вы проиграли!"

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.snake:  Snake| None = self.init_snake()
        self.game_over: bool = False
        self.run: bool = True
        self.count: int = 0
        self.food: Food = self.generate_food()
        self.pause: bool = False

    def inside_field(self, p: Point) -> bool:
        return not(p.x > self.width - 1 or p.x < 0 or p.y > self.height - 1 or p.y < 0)

    def step(self, event: Event):
        self.do_event(event)
        self.game_over = not self.snake.is_correct() or \
                            not self.inside_field(self.snake.head)
        if self.snake.head.intersection(self.food):
            self.food = self.generate_food()
            self.snake.eat()
            self.count += 1

    def do_event(self, event):
        if event.name == Event.UP:
            self.snake.up()
        if event.name == Event.DOWN:
            self.snake.down()
        if event.name == Event.LEFT:
            self.snake.left()
        if event.name == Event.RIGHT:
            self.snake.right()
        if event.name == Event.QUIT:
            self.run = False
        self.snake.move()

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

    def get(self):
        return (self.r, self.g, self.b)


class RenderManager:
    BLACK: Color = Color(0, 0, 0)  # black
    BACKGROUND_COLOR: Color = Color(255, 255, 255)  # white
    SNAKE_COLOR: Color = Color(255, 0, 0)  # red
    MESSAGE_COLOR: Color = Color(0, 255, 0)  # green
    FOOD_COLOR: Color = Color(0, 255, 0)  # green

    def __init__(self, block_size: int, game: Game):
        self.game = game
        self.block_size: int = block_size
        self.screen = pygame.display.set_mode((self.game.width * self.block_size,
                                               self.game.height * self.block_size))
        self.font_style = pygame.font.SysFont(None, 5 * self.block_size)

    def set_caption(self, caption: str):
        pygame.display.set_caption(caption)

    def draw_snake(self):
        # pygame.draw.rect(self.screen, self.SNAKE_COLOR.get(), (self.game.snake.head.x*self.block_size,
        #                                                  self.game.snake.head.y*self.block_size,
        #                                                  self.block_size,
        #                                                  self.block_size))
        for el in self.game.snake.body:
            pygame.draw.rect(self.screen, self.SNAKE_COLOR.get(), (el.x*self.block_size,
                                                                   el.y*self.block_size,
                                                                   self.block_size,
                                                                   self.block_size))

    def draw_food(self):
        pygame.draw.rect(self.screen, self.FOOD_COLOR.get(), [self.game.food.x*self.block_size,
                                                        self.game.food.y*self.block_size,
                                                        self.block_size,
                                                              self.block_size])

    def draw_message(self, msg: str):
        msg = self.font_style.render(msg, True, self.MESSAGE_COLOR.get())
        self.screen.blit(msg, (self.game.width * self.block_size // 2 - msg.get_width() // 2,
                               self.game.height * self.block_size // 2 - msg.get_height() // 2))

    def draw_count(self):
        score = self.font_style.render(f"Счет: {self.game.count}", True, self.MESSAGE_COLOR.get())
        self.screen.blit(score, (0, 0))

    def fill_background(self):
        self.screen.fill(self.BACKGROUND_COLOR.get())

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
        while self.game.run:
            event: Event = self.event_manager.get_event()
            self.game.step(event)

            self.render_manager.fill_background()
            if self.game.game_over:
                self.render_manager.draw_message(self.game.GAME_OVER_MESSAGE)
                self.game.pause = True
                self.render_manager.draw_snake()
                self.render_manager.draw_food()
                self.render_manager.draw_count()
                pygame.display.update()
                if Event.NOTHING:
                    self.clock.tick(1)
                    if self.game.pause == False:
                        break
            self.render_manager.draw_snake()
            self.render_manager.draw_food()
            self.render_manager.draw_count()

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
