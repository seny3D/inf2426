"""
Задача

По списку ребер визуализировать граф с помощью pygame.

Список ребер задается с помощью файла input.txt каждая строка - реберо,
в строке 2 числа - вершины ребра.

Для визуализации графа использовать следующий способ: вершины
отображаем по окружности, а ребрами-линиями их соединяем.
Номер вершины отображать рядом с вершиной на внешней стороне окружности.

"""
from loaders import Loader
from graphs import Graph
from constructors import Constructor
from figures import Figure
from game import RenderManager, GameManager

if __name__ == "__main__":
    graph: Graph = Loader("input.txt").get_graph()
    figure_list: list[Figure] = Constructor(graph).get_figures()
    render_manager: RenderManager = RenderManager()
    game_manager: GameManager = GameManager(render_manager, figure_list)
    game_manager.run()