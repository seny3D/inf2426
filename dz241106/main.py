"""
По списку ребер визулизировать граф c помощью pygame

Список ребер задается с помощью файла input.txt. Каждая строка - ребро,
в строке 2 числа - вершины ребра.

Для визуализации графа использовать следующий способ: вершины
отобраджаем по окружности, а ребрамт - линиями их соединяем.
Номер вершины отображать рядом с вершиной на внешней стороне окружности.
"""
from loaders import Loader
from graphs import Graph
from constructors import Constructor
from figures import Figure
from game import RenderManager, GameManager

if __name__ == '__main__':
    graph: Graph = Loader('input.txt').get_graph()
    figure_list: list[Figure] = Constructor(graph, 20, 25, 2).get_figures()
    render_manager: RenderManager = RenderManager(10)
    game_manager: GameManager = GameManager(render_manager, figure_list)
    game_manager.run()
