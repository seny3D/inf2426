"""
По списку ребер визулизировать граф c помощью pygame

Список ребер задается с помощью файла input.txt. Каждая строка - ребро,
в строке 2 числа - вершины ребра.

Для визуализации графа использовать следующий способ: вершины
отобраджаем по окружности, а ребрамт - линиями их соединяем.
Номер вершины отображать рядом с вершиной на внешней стороне окружности.
"""

from loaders import LoaderEdjacencyList, LoaderEdjacencyMatrix, LoaderEdgeList
from graphs import Graph
from constructors import Constructor, ConstructorGravity
from figures import Figure
from game import RenderManager, GameManager

if __name__ == '__main__':
    graph: Graph = LoaderEdgeList('input.txt').get_graph()
    constructor: ConstructorGravity = ConstructorGravity(graph)
    render_manager: RenderManager = RenderManager()
    game_manager: GameManager = GameManager(render_manager, constructor)
    game_manager.run()
