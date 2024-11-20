from typing import Any, Self, Iterable


class ListNode[T: Any]:
    """
    Элемент связного списка, хранит значения и ссылки на следующий и предыдущий элемент.
    """
    def __init__(self, data: T, prev: Self|None=None, link: Self|None=None) -> None:
        self.data: T = data  # значения
        self.prev: Self|None = prev  # ссылка на предыдущий элемент
        self.link: Self|None = link  # ссылка на следующий элемент

        # Если нам передали ссылку на предыдущий элемент
        if prev is not None:
            # то мы сразу связываем его прямой ссылкой с нами
            self.prev.link = self
        # Если нам передали ссылку на следующий элемент
        if link is not None:
            # то мы связываем его с нами через обратную ссылку
            self.link.prev = self

    def __eq__(self, other) -> bool:
        return self.data == other.data

    def __lt__(self, other) -> bool:
        return self.data < other.data

    def __gt__(self, other) -> bool:
        return self.data > other.data

    def __le__(self, other) -> bool:
        return self.data <= other.data

    def __ge__(self, other) -> bool:
        return self.data >= other.data


class DoubleLinkedList[T: Any]:
    """
    Двусвязный список.
    Добавление и удаление элементов происходит за константу по времени,
    как в начало, так и в конец списка.
    """
    def __init__(self, iter: Iterable|None = None) -> None:
        self._head: ListNode[T]|None = None  # ссылка на первый элемент списка
        self._tail: ListNode[T]|None = None  # ссылка на последний элемент списка
        self._length: int = 0  # длинна списка
        if iter is not None:
            self._from_iter(iter)

    def _from_iter(self, iter: Iterable) -> None:
        for el in iter:
            self.add_last(el)

    def __len__(self) -> int:
        return self._length

    def _add_between(self, item: T, before: ListNode[T]|None, after: ListNode[T]|None) -> None:
        """
        Добавляем элемент в список, между заданными соседними элементами списка.
        Так же корректно работает при вставке первого и последнего элемента,
        если одного из соседних элементов указать как None.
        :param item: новое значение
        :param before: элемент, после которого надо вставить новый
        :param after: элемент, перед которым надо вставить новый
        :return: None
        """
        # создаем элемент списка для нового значения
        # при создании элемента уже установятся корректные
        # ссылки на следующий и предыдущий элементы
        node: ListNode[T] = ListNode(item, before, after)
        # Если новый элемент вставлен до первого
        if after is self._head:
            # то он стал первым элементом
            self._head = node
        # Если новый элемент вставлен после посленего
        if before is self._tail:
            # то он стал последним элементом
            self._tail = node
        # Увеличиваем длинну списка
        self._length += 1

    def add_first(self, item: T) -> None:
        """
        Вставляем новое значение в начало списка
        :param item: новое значение
        :return: None
        """
        # Вставку в началоа элемента можно мыслить
        # как вставку между None и первым элементом
        self._add_between(item, None, self._head)

    def add_last(self, item: T) -> None:
        """
        Добавляем новое значение в конец списка
        :param item: новое значение
        :return: None
        """
        # Вставку в конец элемента можно мыслить
        # как вставку между последним элементом и None
        self._add_between(item, self._tail, None)

    def _remove(self, node: ListNode[T]|None) -> T:
        """
        Удаляет элемент node в списке, и возвращает его значение
        :param node: ссылка на элемент
        :return: значение элемента, который удалили
        """
        # запоминаем какой элемент перед удаляемым
        try:
            before: ListNode[T]|None = node.prev
        except AttributeError:
            # если пытаются что-то удалить из пустого списка
            # выбрасываем исключение
            raise RuntimeError("double linked list is empty")
            # дальше выполнение не идет, программа останавливается
        # и какой после него
        after: ListNode[T]|None = node.link
        # Если удаляем первый элемент
        if node is self._head:
            # то первым элементом становится следующий элемент
            # за удаляемым
            self._head = after
        else:
            # иначе, тому кто перед удаляемым элементом,
            # нужно ссылаться на следующий после удаляемого
            before.link = after
        # Если удаляем последний элемент
        if node is self._tail:
            # То предпоследний становится последним
            self._tail = before
        else:
            # Иначе предыдущим для следующего за удаляемым элементом
            # становит, предыдущий к удаляемому
            after.prev = before
        # Уменьшаем длинну списка
        self._length -= 1
        # Возвращаем значение удаленного элемента
        return node.data

    def remove_first(self) -> T:
        """
        Удаляем первый элемент списка
        :return: значение первого элемента
        """
        return self._remove(self._head)

    def remove_last(self) -> T:
        """
        Удаляем последний элемент списка
        :return: значение последнего элемента
        """
        return self._remove(self._tail)

    def to_list(self) -> list[T]:
        """
        Возвращает двусвязный список в виде списка Python
        :return: список Python
        """
        res: list[T] = []
        current: ListNode[T] = self._head
        while current is not None:
            res.append(current.data)
            current = current.link
        return res

    def __str__(self) -> str:
        return str(tuple(self.to_list()))

    def _peek(self, node: ListNode) -> T:
        """
        Возвращает значение элемента
        :param node: элемент
        :return: значение
        """
        return node.data

    def peek_last(self) -> T:
        """
        Возвращает значение последнего элемента
        :return: значение
        """
        return self._peek(self._tail)

    def peek_first(self) -> T:
        """
        Возвращает значение первого элемента
        :return: значение
        """
        return self._peek(self._head)

    def _cmp(self, other: Self) -> int:
        """
        Сравнение двух объектов двусвязных списков,
        возвращает число больше нуля если  self > other
        равное нулю, если self == other
        и меньше нуля, если self < other
        :param other:
        :return:
        """
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...

    def __ge__(self, other) -> bool:
        ...

    def __le__(self, other) -> bool:
        ...

    def slow_sort(self) -> None:
        """
        Сортировка двусвязного списка за O(n**2)
        Список сортируется за константу по памяти.
        Ничего не возвращает. Изменяет сам список.
        :return: None
        """
        ...

    def sort(self) -> None:
        """
        Сортировка двусвязного списка за O(nlogn)
        Список сортируется за константу по памяти.
        Ничего не возвращает. Изменяет сам список.
        :return: None
        """
        ...


class LinkedBase[T: Any]:
    """
    Класс реализующий общие методы для стека и очереди
    """
    def __init__(self):
        self._list: DoubleLinkedList[T] = DoubleLinkedList()

    def peek(self) -> T:
        return self._list.peek_last()

    def __len__(self) -> int:
        return len(self._list)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __str__(self):
        return str(self._list)


class LinkedQueue[T: Any](LinkedBase):
    """
    Очередь на двусвязном списке
    """
    def enqueue(self, item: T) -> None:
        self._list.add_first(item)

    def dequeue(self) -> T:
        return self._list.remove_last()



class LinkedStack[T: Any](LinkedBase):
    """
    Стек на двусвязном списке
    """
    def push(self, item: T) -> None:
        self._list.add_last(item)

    def pop(self) -> T:
        return self._list.remove_last()


if __name__ == "__main__":
    a: DoubleLinkedList[int] = DoubleLinkedList([1,2,3,4])
    print(a)
    a.add_first(-5)
    print(a)
    a.add_last(10)
    print(a)
    a.remove_last()
    print(a)
    a.remove_first()
    print(a)
    a.remove_first()
    a.remove_first()
    print(a)
    a.remove_last()
    a.remove_last()
    print(len(a))
    try:
        a.remove_last()
    except RuntimeError as err:
        print(err)
        print("не получилось удалить из пустого списка")
    print(a)
    a.add_first(4)
    a.add_first(3)
    print(a)
    a.add_last(5)
    a.add_last(6)
    print(a)

    c: ListNode[int] = ListNode(5)
    d: ListNode[int] = ListNode(6)
    print(d > c)
    print(d == c)
    print(d < c)
    print(d >= c)
    print(d <= c)
