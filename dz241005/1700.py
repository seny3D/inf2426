#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=EASY
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        from typing import Any, Self, Iterable
        class ListNode:
            def __init__(self, data: Any, prev: Self | None = None, link: Self | None = None) -> None:
                self.data: Any = data  # значения
                self.prev: Self | None = prev  # ссылка на предыдущий элемент
                self.link: Self | None = link  # ссылка на следующий элемент

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

            def __init__(self, iter: Iterable | None = None) -> None:
                self._head: ListNode | None = None  # ссылка на первый элемент списка
                self._tail: ListNode | None = None  # ссылка на последний элемент списка
                self._length: int = 0  # длинна списка
                if iter is not None:
                    self._from_iter(iter)

            def _from_iter(self, iter: Iterable) -> None:
                for el in iter:
                    self.add_last(el)

            def __len__(self) -> int:
                return self._length

            def _add_between(self, item: Any, before: ListNode | None, after: ListNode | None) -> None:
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

            def add_last(self, item: Any) -> None:
                # Вставку в конец элемента можно мыслить
                # как вставку между последним элементом и None
                self._add_between(item, self._tail, None)

            def add_first(self, item: Any) -> None:
                # Вставку в начало элемента можно мыслить
                # как вставку между None и первым элементом
                self._add_between(item, None, self._head)

            def _remove(self, node: ListNode | None) -> Any:
                """
                Удаляет элемент node в списке, и возвращает его значение
                :param node: ссылка на элемент
                :return: значение элемента, который удалили
                """
                # запоминаем какой элемент перед удаляемым
                try:
                    before: ListNode | None = node.prev
                except AttributeError:
                    # если пытаются что-то удалить из пустого списка
                    # выбрасываем исключение
                    raise RuntimeError("double linked list is empty")
                    # дальше выполнение не идет, программа останавливается
                # и какой после него
                after: ListNode | None = node.link
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

            def remove_first(self) -> Any:
                """
                Удаляем первый элемент списка
                :return: значение первого элемента
                """
                return self._remove(self._head)

            def _peek(self, node: ListNode) -> Any:
                """
                Возвращает значение элемента
                :param node: элемент
                :return: значение
                """
                return node.data

            def peek_first(self) -> Any:
                """
                Возвращает значение первого элемента
                :return: значение
                """
                return self._peek(self._head)

            def peek_last(self) -> Any:
                """
                Возвращает значение последнего элемента
                :return: значение
                """
                return self._peek(self._tail)

        class LinkedBase:
            def __init__(self):
                self._list: DoubleLinkedList = DoubleLinkedList()

            def peek(self) -> Any:
                return self._list.peek_first()

            def __len__(self) -> int:
                return len(self._list)

            def is_empty(self) -> bool:
                return len(self) == 0

            def __str__(self):
                return str(self._list)

        class LinkedQueue(LinkedBase):
            def enqueue(self, item: Any) -> None:
                self._list.add_last(item)

            def dequeue(self) -> Any:
                return self._list.remove_first()

        class LinkedStack(LinkedBase):
            def push(self, item: Any) -> None:
                self._list.add_first(item)

            def pop(self) -> Any:
                return self._list.remove_first()

        len_studies: int = len(students)
        studies: LinkedQueue = LinkedQueue()
        sandwichess: LinkedStack = LinkedStack()
        for i in range(len_studies - 1, -1, -1):
            studies.enqueue(students[i])
            sandwichess.push(sandwiches[i])
        n: int = 0
        while n < len_studies:
            if len_studies > 0:
                st_head: int = studies.peek()
                san_head: int = sandwichess.peek()
                if st_head == san_head:
                    n = 0
                    len_studies -= 1
                    studies.dequeue()
                    sandwichess.pop()
                else:
                    n += 1
                    studies.enqueue(st_head)
                    studies.dequeue()
            else:
                return 0
        return len_studies