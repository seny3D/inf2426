from typing import Iterable
from graphs import Graph

class FileReader:
    def __init__(self, filen: str) -> None:
        self.filen: str = filen

    def read_all(self) -> Iterable[tuple[int, int]]:
        with open(self.filen, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                v1: str
                v2: str
                v1, v2 = line.split()
                yield int(v1), int(v2)


class Loader:
    """
    Считывет список ребер и возвращает граф
    """
    def __init__(self, filen: str) -> None:
        self.file_reader: FileReader = FileReader(filen)
        self.graph: Graph = Graph()

    def get_graph(self) -> Graph:
        for v1, v2 in self.file_reader.read_all():
            self.graph.add_edge(v1, v2)
        return self.graph
