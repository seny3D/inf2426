#https://leetcode.com/problems/next-greater-element-i/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=EASY
from typing import Any, Self, Iterable
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]):
        class ListNode:
            """
            Элемент связного списка, хранит значения и ссылки на следующий и предыдущий элемент.
            """

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
                while cur_self is not None and cur_other is not None:  # проверяем, что оба объекта хранят какую то data
                    if cur_self < cur_other:
                        return -1
                    elif cur_self > cur_other:
                        return 1
                    # берем следующий элемент двусвязного списка
                    cur_self = cur_self.link
                    cur_other = cur_other.link
                # если один список является подсписком другого, то большим является список, у которого \
                # большее кол - во элементов
                if cur_self is not None:  # если во втором двусвязном списке кончились элементы, а в первом еще есть \
                    return 1  # то возвращаем 1
                elif cur_other is not None:  # если в первом двусвязном списке кончились элементы, а в первом еще есть \
                    return -1  # то возвращаем -1
                else:
                    return 0  # возвращаем 0, если списки полностью идентичны

            def __lt__(self, other: Self) -> bool:
                return self._cmp(other) == -1

            def __gt__(self, other: Self) -> bool:
                return self._cmp(other) == 1

            def __eq__(self, other: Self) -> bool:
                return self._cmp(other) == 0

            def __ge__(self, other: Self) -> bool:
                return self._cmp(other) in [0, 1]

            def __le__(self, other: Self) -> bool:
                return self._cmp(other) in [0, -1]

            def slow_sort(self) -> None:
                """
                Сортировка двусвязного списка за O(n**2)
                Список сортируется за константу по памяти.
                Ничего не возвращает. Изменяет сам список.
                :return: None
                """
                cur1: ListNode = self._head  # элемент для нужного количества проходов по списку. когда достигнет конца списка, сортировка завершится
                while cur1 is not None:
                    cur2: ListNode = self._head  # берем начальный элемент двусвязного списка
                    while cur2.link is not None:  # проверка, не дошли ли до конца списка
                        if cur2 > cur2.link:  # если один элемент больше другого, то меняем их местами
                            self._remove(cur2)
                            self._add_between(cur2.data, cur2.link, cur2.link.link)
                        cur2 = cur2.link  # берем следующий элемент
                    cur1 = cur1.link  # берем следующий элемент

        class LinkedBase:
            """
            Класс реализующий общие методы для стека и очереди
            """

            def __init__(self, datas: list[Any] | None = None):
                self._list: DoubleLinkedList = DoubleLinkedList(datas)

            def peek(self) -> Any:
                return self._list.peek_last()

            def __len__(self) -> int:
                return len(self._list)

            def is_empty(self) -> bool:
                return len(self) == 0

            def __str__(self):
                return str(self._list)

        class LinkedStack(LinkedBase):
            """
            Стек на двусвязном списке
            """

            def push(self, item: Any) -> None:
                self._list.add_last(item)

            def pop(self) -> Any:
                return self._list.remove_last()

        nums3: list[list[int]] = []
        for i in range(len(nums2)):
            m: int = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    m = nums2[j]
                    break
            nums3.append([nums2[i], m])
        stack1: LinkedStack = LinkedStack(nums3[::-1])
        stack2: LinkedStack = LinkedStack()
        ans: list[int] = []
        for i in range(len(nums1)):
            if stack2.is_empty():
                if stack1.peek()[0] == nums1[i]:
                    ans.append(stack1.peek()[1])
                    stack1.pop()
                    continue
                while not stack1.is_empty():
                    stack2.push(stack1.pop())
                    if stack2.peek()[0] == nums1[i]:
                        ans.append(stack2.peek()[1])
                        stack2.pop()
            if stack1.is_empty():
                if stack2.peek()[0] == nums1[i]:
                    ans.append(stack2.peek()[1])
                    stack2.pop()
                    continue
                while not stack2.is_empty():
                    stack1.push(stack2.pop())
                    if stack1.peek()[0] == nums1[i]:
                        ans.append(stack1.peek()[1])
                        stack1.pop()

        return ans

