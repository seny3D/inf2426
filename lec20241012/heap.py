from typing import Any


class ListNode:
    ...


class Heap[T: Any]:
    def _cmp(self, o1: T, o2: T) -> int:
        ...

    def insert(self, o: T) -> None:
        ...

    def get_max(self) -> T:
        ...

    def extract_max(self) -> T:
        ...


class HeapMin[T: Any](Heap):
    def _cmp(self, o1: T, o2: T) -> int:
        ...

    def get_min(self) -> T:
        return self.get_max()

    def extract_min(self) -> T:
        return self.extract_max()


class Data[T: Any]:
    def __init__(self, data: T, priority: int):
        self.data: T = data
        self.priority: int = priority


class QueueWithPriority[T: Any]:
    def enqueue(self, data: T, priority: int) -> None:
        """Adds an element to the rear of the queue."""

    def dequeue(self) -> T:
        """Removes and returns the element from the front of the queue."""

    def peek(self) -> T:
        """Returns the element at the front of the queue without removing it."""

    def empty(self) -> bool:
        """Checks if the queue is empty."""

