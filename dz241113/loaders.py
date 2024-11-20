from typing import Iterable


from graphs import Graph

class IReader:
    def read_all(self) -> Iterable[tuple[str, str]]:
        raise NotImplementedError()


class FileReaderEdgeList:
    def __init__(self, filen: str) -> None:
        self.filen: str = filen

    def read_all(self) -> Iterable[tuple[str, str]]:
        with open(self.filen, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                v1: str
                v2: str
                v1, v2 = line.split()
                yield v1, v2

class FileReaderEdjacencyList:
    def __init__(self, filen: str) -> None:
        self.filen: str = filen

    def read_all(self) -> Iterable[tuple[str, str]]:
        with open(self.filen, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                v: str
                edg: list[str]
                v, *edg = line.split()
                yield v, edg

class FileReaderMatrixList:
    def __init__(self, filen: str) -> None:
        self.filen: str = filen

    def read_all(self) -> Iterable[tuple[str, str]]:
        with open(self.filen, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                v: str
                edg: list[str]
                v, *edg = line.split()
                yield v, edg

class ILoader:
    """
    общий интерфейс для классов-загрузчиков графов в разных представлениях
    """
    def get_graph(self) -> Graph:
        raise NotImplementedError()

class LoaderEdgeList(ILoader):
    def __init__(self, filen: str) -> None:
        self.file_reader: FileReaderEdgeList = FileReaderEdgeList(filen)
        self.graph: Graph = Graph()

    def get_graph(self) -> Graph:
        for v1, v2 in self.file_reader.read_all():
            self.graph.add_edge(v1, v2)
        return self.graph

class LoaderEdjacencyList(ILoader):
    def __init__(self, filen: str) -> None:
        self.file_reader: FileReaderEdjacencyList = FileReaderEdjacencyList(filen)
        self.graph: Graph = Graph()

    def get_graph(self) -> Graph:
        for v1, edg in self.file_reader.read_all():
            self.graph.add_vertex(v1, edg)
        return self.graph

class LoaderEdjacencyMatrix(ILoader):
    def __init__(self, filen: str) -> None:
        self.file_reader: FileReaderMatrixList = FileReaderMatrixList(filen)
        self.graph: Graph = Graph()
        self.matrix: list[str] = []

    def get_graph(self) -> Graph:
        self.matrix.extend(self.file_reader.read_all())
        for x in range(len(self.matrix)):
            this: str = self.matrix[x][0]
            for i in range(len(self.matrix[1])):
                newg: str = self.matrix[i - 1][0]
                if self.matrix[x][1][i] == '1':
                    self.graph.add_edge(this, newg)
        return self.graph

