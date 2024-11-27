from collections import defaultdict
from collections.abc import Iterable


class Graph:
    """
    Представление графа
    """
    def __init__(self):
        self.g = defaultdict(list)

    def add_edge(self, v1:int, v2:int) -> None:
        self.g[v1].append(v2)
        self.g[v2].append(v1)

    @property
    def vertices(self) -> Iterable[int]:
        for k in self.g:
            yield k

    def get_adjacents(self, v: int) -> list[int]:
        return self.g[v]

    def __len__(self):
        return len(self.g)