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

    def __iadd__(self, other: Self) -> Self:
        return self + other

    def intersection(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y


class Food(Point):
    pass


class Stone(Point):
    pass


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
    RESTART: str = "restart"

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
    GAME_OVER_MESSAGE: str = "Вы проиграли!"

    def __init__(self, width: int, height: int, stone_count: int):
        self.width: int = width
        self.height: int = height
        self.snake: Snake | None = self.init_snake()
        self.game_over: bool = False
        self.run: bool = True
        self.stones: list[Stone] = self.generate_stones(stone_count)
        self.food: Food = self.generate_food()
        self.count: int = 0

    def inside_field(self, p: Point) -> bool:
        return not (p.x > self.width - 1 or p.x < 0 or p.y > self.height - 1 or p.y < 0)

    def step(self, event: Event):
        if self.game_over and event.name == Event.RESTART:
            self.restart()
        else:
            self.do_event(event)
            self.game_over = not self.snake.is_correct() or not self.inside_field(self.snake.head)

            if self.snake.head.intersection(self.food):
                self.food = self.generate_food()
                self.snake.eat()
                self.count += 1

            for stone in self.stones:
                if self.snake.head.intersection(stone):
                    self.game_over = True

    def do_event(self, event):
        if self.game_over:
            if event.name == Event.QUIT:
                self.run = False
            elif event.name != Event.NOTHING:
                self.restart()
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
        while True:
            x: int = random.randint(0, self.width - 1)
            y: int = random.randint(0, self.height - 1)
            food = Food(x, y)

            if all((food.x != stone.x or food.y != stone.y) for stone in
                   self.stones):  # чтобы еда в камне не спавнилась
                return food

    def restart(self):
        self.game_over = False
        self.run = True
        self.snake = self.init_snake()
        self.stones = self.generate_stones(random.randint(1, 100))
        self.food = self.generate_food()
        self.food = self.generate_food()
        self.count: int = 0

    def generate_stones(self, count: int) -> list[Stone]:
        stones = []
        busyplace = set()

        while len(stones) < count:
            x: int = random.randint(0, self.width - 1)
            y: int = random.randint(0, self.height - 1)

            if x not in busyplace and y not in busyplace:
                newstone = Stone(x, y)
                stones.append(newstone)
                busyplace.add((x, y))

        return stones

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
        return self.r, self.g, self.b


class Gamer:
    def __init__(self, game: Game):
        self.game = game

    def get_next_event(self) -> Event:
        # находим расстояние между головой змеи и еды
        dx = self.game.food.x - self.game.snake.head.x
        dy = self.game.food.y - self.game.snake.head.y

        # выбираем ось x как основную
        if abs(dx) > abs(dy):
            if dx > 0 and self.can_move(Point(1, 0)):
                return Event(Event.RIGHT)
            elif dx < 0 and self.can_move(Point(-1, 0)):
                return Event(Event.LEFT)
        # движение по y
        if dy > 0 and self.can_move(Point(0, 1)):
            return Event(Event.DOWN)
        elif dy < 0 and self.can_move(Point(0, -1)):
            return Event(Event.UP)

        if any(self.game.snake.head.intersection(body) for body in
               list(self.game.snake.body)[:-1]):  # проверка на столкновение
            return Event(Event.RESTART)

        # прямой путь закрыт выбираем обходное направление
        return self.skip_prep()

    def can_move(self, direction: Point) -> bool:  # проверка можем ли двигаться
        next_position = self.game.snake.head + direction
        return (self.game.inside_field(next_position) and
                all(not next_position.intersection(stone) for stone in self.game.stones) and
                not any(body.intersection(next_position) for body in self.game.snake.body))

    def skip_prep(self) -> Event:  # избегаем препятствия
        # обход препятствия
        directions = [Event.UP, Event.DOWN, Event.LEFT, Event.RIGHT]
        random.shuffle(directions)  # двигаемся в случайном направлении

        for direction in directions:
            point_direction = self.pointdir(direction)
            if self.can_move(point_direction):
                return Event(direction)

        # случай если невозможно двигаться
        return Event(Event.NOTHING)

    def pointdir(self, direction: str) -> Point:
        if direction == Event.UP:
            return Point(0, -1)
        elif direction == Event.DOWN:
            return Point(0, 1)
        elif direction == Event.LEFT:
            return Point(-1, 0)
        elif direction == Event.RIGHT:
            return Point(1, 0)
        return Point(0, 0)


class RenderManager:
    BLACK: Color = Color(0, 0, 0)
    BACKGROUND_COLOR: Color = Color(0, 0, 0)
    SNAKE_COLOR: Color = Color(0, 255, 0)
    MESSAGE_COLOR: Color = Color(0, 255, 0)
    COUNT_COLOR: Color = Color(123, 123, 123)
    FOOD_COLOR: Color = Color(255, 0, 0)
    STONE_COLOR: Color = Color(255, 255, 255)

    def __init__(self, block_size: int, game: Game):
        self.game = game
        self.block_size: int = block_size
        self.screen = pygame.display.set_mode((self.game.width * self.block_size,
                                               self.game.height * self.block_size))
        self.font_style = pygame.font.SysFont(None, 5 * self.block_size)

    def set_caption(self, caption: str):
        pygame.display.set_caption(caption)

    def draw_snake(self):
        for el in self.game.snake.body:
            pygame.draw.rect(self.screen, self.SNAKE_COLOR.get(), (el.x * self.block_size,
                                                                   el.y * self.block_size,
                                                                   self.block_size,
                                                                   self.block_size))

    def draw_food(self):
        pygame.draw.ellipse(self.screen, self.FOOD_COLOR.get(), [self.game.food.x * self.block_size,
                                                                 self.game.food.y * self.block_size,
                                                                 self.block_size,
                                                                 self.block_size])

    def draw_count(self):
        score = self.font_style.render(f"Счет: {self.game.count}", True, self.COUNT_COLOR.get())
        self.screen.blit(score, (0, 0))

    def draw_stones(self):
        for stone in self.game.stones:
            pygame.draw.rect(self.screen, self.STONE_COLOR.get(), (stone.x * self.block_size,
                                                                   stone.y * self.block_size,
                                                                   self.block_size,
                                                                   self.block_size))

    def draw_message(self, msg: str):
        msg = self.font_style.render(msg, True, self.MESSAGE_COLOR.get())
        self.screen.blit(msg, (self.game.width * self.block_size // 2 - msg.get_width() // 2,
                               self.game.height * self.block_size // 2 - msg.get_height() // 2))

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
                if event.name not in (Event.QUIT and Event.NOTHING) and self.game.game_over:
                    self.game.restart()
                else:
                    self.game.restart()
            self.render_manager.draw_snake()
            self.render_manager.draw_stones()
            self.render_manager.draw_food()
            self.render_manager.draw_count()

            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()
        quit()


if __name__ == "__main__":
    g = Game(80, 60, stone_count=random.randint(0, 100))
    autopilot = Gamer(g)  # Создаем автопилот
    manager = GameManager(EventManager, g, RenderManager, fps=300, caption="Игра Змейка")

    while g.run:
        event = autopilot.get_next_event()
        g.step(event)
        manager.render_manager.fill_background()
        manager.render_manager.draw_snake()
        manager.render_manager.draw_food()
        manager.render_manager.draw_count()
        manager.render_manager.draw_stones()
        pygame.display.update()
        manager.clock.tick(manager.fps)

    pygame.quit()
