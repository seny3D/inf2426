from collections import defaultdict
from typing import List, DefaultDict, Iterable

class Graph:
    """
    Представление графа
    """
    def __init__(self):
        self.g: DefaultDict[str, List[str]] = defaultdict(list)

    def add_edge(self, v1: str, v2: str) -> None:
        self.g[v1].append(v2)
        self.g[v2].append(v1)
        
    def add_vertex(self, v: str, edg: list[str]) -> None:
        self.g[v] = edg
    @property
    def vehicles(self) -> Iterable[str]:
        return self.g.keys()

    def get_adjacents(self, v: str) -> list[str]:
        return self.g[v]
    
    def __len__(self):
        return len(self.g)

