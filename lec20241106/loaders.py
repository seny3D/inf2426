from typing import Iterable

from graphs import Graph


class FileReader:
    def __init__(self, file: str):
        self.file = file

    def read_all(self) -> Iterable[tuple[int, int]]:
        with open(self.file, "r", encoding="utf-8") as f:
            for line in f.readlines():
                v1, v2 = line.split()
                yield int(v1), int(v2)


class Loader:
    """
    Считывает список ребер и возвращает граф
    """
    def __init__(self, file: str):
        self.file_reader = FileReader(file)
        self.graph = Graph()

    def get_graph(self) -> Graph:
        for v1, v2 in self.file_reader.read_all():
            self.graph.add_edge(v1, v2)
        return self.graph