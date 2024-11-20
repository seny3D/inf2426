#https://leetcode.com/problems/design-hashset/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=EASY
from typing import Any, Iterable, Self
class ListNode:
    """
    Элемент связного списка, хранит значения и ссылки на следующий и предыдущий элемент.
    """
    def __init__(self, data: Any, prev: Self|None=None, link: Self|None=None) -> None:
        self.data: Any = data  # значения
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


class DoubleLinkedList:
    """
    Двусвязный список.
    Добавление и удаление элементов происходит за константу по времени,
    как в начало, так и в конец списка.
    """
    def __init__(self, iter: Iterable|None = None) -> None:
        self._head: ListNode|None = None  # ссылка на первый элемент списка
        self._tail: ListNode|None = None  # ссылка на последний элемент списка
        self._length: int = 0  # длинна списка
        if iter is not None:
            self._from_iter(iter)

    def _from_iter(self, iter: Iterable) -> None:
        for el in iter:
            self.add_last(el)

    def __len__(self) -> int:
        return self._length

    def _add_between(self, item: Any, before: ListNode|None, after: ListNode|None) -> None:
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
        node: ListNode = ListNode(item, before, after)
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

    def add_first(self, item: Any) -> None:
        """
        Вставляем новое значение в начало списка
        :param item: новое значение
        :return: None
        """
        # Вставку в начало элемента можно мыслить
        # как вставку между None и первым элементом
        self._add_between(item, None, self._head)

    def add_last(self, item: Any) -> None:
        """
        Добавляем новое значение в конец списка
        :param item: новое значение
        :return: None
        """
        # Вставку в конец элемента можно мыслить
        # как вставку между последним элементом и None
        self._add_between(item, self._tail, None)

    def _remove(self, node: ListNode|None) -> Any:
        """
        Удаляет элемент node в списке, и возвращает его значение
        :param node: ссылка на элемент
        :return: значение элемента, который удалили
        """
        # запоминаем какой элемент перед удаляемым
        try:
            before: ListNode|None = node.prev
        except AttributeError:
            # если пытаются что-то удалить из пустого списка
            # выбрасываем исключение
            raise RuntimeError("double linked list is empty")
            # дальше выполнение не идет, программа останавливается
        # и какой после него
        after: ListNode|None = node.link
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
        # Уменьшаем длину списка
        self._length -= 1
        # Возвращаем значение удаленного элемента
        return node.data

    def remove_first(self) -> Any:
        """
        Удаляем первый элемент списка
        :return: значение первого элемента
        """
        return self._remove(self._head)

    def remove_last(self) -> Any:
        """
        Удаляем последний элемент списка
        :return: значение последнего элемента
        """
        return self._remove(self._tail)

    def to_list(self) -> list[Any]:
        """
        Возвращает двусвязный список в виде списка Python
        :return: список Python
        """
        res: list[Any] = []
        current: ListNode = self._head
        while current is not None:
            res.append(current.data)
            current = current.link
        return res

    def __str__(self) -> str:
        return str(tuple(self.to_list()))

    def _peek(self, node: ListNode) -> Any:
        """
        Возвращает значение элемента
        :param node: элемент
        :return: значение
        """
        return node.data

    def peek_last(self) -> Any:
        """
        Возвращает значение последнего элемента
        :return: значение
        """
        return self._peek(self._tail)

    def peek_first(self) -> Any:
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
        cur_self: ListNode = self._head
        cur_other: ListNode = other._head
        while cur_self is not None and cur_other is not None:
            if cur_self < cur_other:
                return -1
            elif cur_self > cur_other:
                return 1
            cur_self = cur_self.link
            cur_other = cur_other.link
        if cur_self is not None:
            return 1
        elif cur_other is not None:
            return -1
        else:
            return 0
    def __lt__(self, other: Self) -> bool:
        return self._cmp(other) == -1

    def __gt__(self, other: Self) -> bool:
        return self._cmp(other) == 1

    def __eq__(self, other: Self) -> bool:
        return self._cmp(other) == 0

    def __ge__(self, other: Self) -> bool:
        return self._cmp(other) in [0,1]

    def __le__(self, other: Self) -> bool:
        return self._cmp(other) in [0,-1]

    def key_in_dll(self, key: int) -> bool:
        cur: ListNode = self._head
        while cur is not None:
            if cur.data == key:
                return True
            cur = cur.link
        return False

    def new_key_in_dll(self, key: int) -> ListNode|None:
        cur: ListNode = self._head
        while cur is not None:
            if cur.data == key:
                return cur
            cur = cur.link
        return None
class MyHashSet:

    def __init__(self):
        self.list: list[DoubleLinkedList] = [DoubleLinkedList() for i in range(1000)]

    def add(self, key: int) -> None:
        if not self.list[self.hash(key)].key_in_dll(key):
            self.list[self.hash(key)].add_last(key)
    def remove(self, key: int) -> None:
        if self.list[self.hash(key)].key_in_dll(key):
            self.list[self.hash(key)]._remove(self.list[self.hash(key)].new_key_in_dll(key))
    def contains(self, key: int) -> bool:
        return self.list[self.hash(key)].key_in_dll(key)

    def hash(self, key: int) -> int:
        return key%1000







