from typing import Any

class ListNode:
    ...


class BST[T: Any]:
    def __init__(self, a: list[T] = None) -> None:
        ...
        if a is not None:
            self.from_list(a)
        ...

    def from_list(self, a: list[T]) -> None:
        ...

    def search(self, o: T) -> bool:
        ...

    def insert(self, o: T) -> None:
        ...

    def delete(self, o: T) -> None:
        ...