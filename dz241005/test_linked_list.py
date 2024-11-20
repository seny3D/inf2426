import unittest
from tokenize import Double
from unittest import TestCase
from linked_list import DoubleLinkedList, ListNode, LinkedQueue, LinkedStack


class TestListNode(TestCase):
    def test_create(self):
        a = ListNode(5)
        self.assertEqual(5, a.data)

    def test_create2(self):
        a = ListNode(5)
        b = ListNode(7)
        c = ListNode(6, a, b)
        self.assertEqual(True, c.link is b)

    def test_create3(self):
        a = ListNode(5)
        b = ListNode(7)
        c = ListNode(6, a, b)
        self.assertEqual(True, c.prev is a)

    def test_create4(self):
        a = ListNode(5)
        b = ListNode(7)
        c = ListNode(6, a, b)
        self.assertEqual(True, a.link is c)

    def test_create5(self):
        a = ListNode(5)
        b = ListNode(7)
        c = ListNode(6, a, b)
        self.assertEqual(True, b.prev is c)

    def test_eq(self):
        a = ListNode(5)
        b = ListNode(5)
        self.assertEqual(True, a == b)

    def test_not_eq(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(False, a == b)

    def test_less(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(True, a < b)

    def test_not_less(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(False, b < a)

    def test_greater(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(True, b > a)

    def test_not_greater(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(False, a > b)

    def test_less_or_equal(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(True, a <= b)

    def test_less_or_equal2(self):
        a = ListNode(5)
        b = ListNode(5)
        self.assertEqual(True, a <= b)

    def test_not_less_or_equal(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(False, b <= a)

    def test_greater_or_equal(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(True, b >= a)

    def test_greater_or_equal2(self):
        a = ListNode(6)
        b = ListNode(6)
        self.assertEqual(True, b >= a)

    def test_not_greater_or_equal(self):
        a = ListNode(5)
        b = ListNode(6)
        self.assertEqual(False, a >= b)


class TestDoubleLinkedList(TestCase):
    def test_add_last(self):
        a = DoubleLinkedList()
        a.add_last(5)
        # Последний элемент это элемент списка
        self.assertEqual(True, isinstance(a._tail, ListNode))

    def test_add_last2(self):
        a = DoubleLinkedList()
        a.add_last(5)
        # первый и последний элемент совпадают
        self.assertEqual(True, a._tail is a._head)

    def test_add_last3(self):
        a = DoubleLinkedList()
        a.add_last(5)
        # в последнем элементе лежит 5
        self.assertEqual(5, a._tail.data)

    def test_to_list(self):
        a = DoubleLinkedList()
        self.assertEqual([], a.to_list())

    def test_to_list2(self):
        a = DoubleLinkedList()
        a.add_last(1)
        self.assertEqual([1], a.to_list())

    def test_str(self):
        a = DoubleLinkedList()
        a.add_last(1)
        self.assertEqual('(1,)', str(a))

    def test_create_from_list(self):
        a = DoubleLinkedList([1,2,3,4,5])
        self.assertEqual([1,2,3,4,5], a.to_list())

    def test_add_last4(self):
        a = DoubleLinkedList()
        a.add_last(5)
        a.add_last(6)
        self.assertEqual([5,6], a.to_list())

    def test_add_first(self):
        a = DoubleLinkedList()
        a.add_first(5)
        self.assertEqual([5], a.to_list())

    def test_add_first2(self):
        a = DoubleLinkedList([1,2])
        a.add_first(5)
        self.assertEqual([5,1,2], a.to_list())

    def test_add_first3(self):
        a = DoubleLinkedList()
        a.add_first(5)
        a.add_first(6)
        self.assertEqual([6,5], a.to_list())

    def test_len(self):
        a = DoubleLinkedList([1,2,3])
        self.assertEqual(3, len(a))

    def test_remove_last(self):
        a = DoubleLinkedList([1,2,3])
        b = a.remove_last()
        self.assertEqual(3, b)

    def test_remove_last2(self):
        a = DoubleLinkedList([1,2,3])
        b = a.remove_last()
        self.assertEqual([1,2], a.to_list())

    def test_remove_last3(self):
        a = DoubleLinkedList()
        self.assertRaises(RuntimeError, a.remove_last)

    def test_remove_first(self):
        a = DoubleLinkedList([1,2,3])
        b = a.remove_first()
        self.assertEqual(1, b)

    def test_remove_first2(self):
        a = DoubleLinkedList([1,2,3])
        b = a.remove_first()
        self.assertEqual([2,3], a.to_list())

    def test_remove_first3(self):
        a = DoubleLinkedList()
        self.assertRaises(RuntimeError, a.remove_first)

    def test_peek_last(self):
        a = DoubleLinkedList([1,2,3])
        b = a.peek_last()
        self.assertEqual(3, b)

    def test_peek_last2(self):
        a = DoubleLinkedList([1,2,3])
        b = a.peek_last()
        self.assertEqual([1,2,3], a.to_list())

    def test_peek_first(self):
        a = DoubleLinkedList([1,2,3])
        b = a.peek_first()
        self.assertEqual(1, b)

    def test_peek_first2(self):
        a = DoubleLinkedList([1,2,3])
        b = a.peek_first()
        self.assertEqual([1,2,3], a.to_list())

    def test_eq(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,3])
        self.assertEqual(True, a == b)

    def test_not_eq(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,4])
        self.assertEqual(False, a == b)

    def test_less(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,3,3])
        self.assertEqual(True, a < b)

    def test_not_less(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([2,2,3])
        self.assertEqual(False, b < a)

    def test_greater(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,4])
        self.assertEqual(True, b > a)

    def test_not_greater(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,5])
        self.assertEqual(False, a > b)

    def test_less_or_equal(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,6])
        self.assertEqual(True, a <= b)

    def test_less_or_equal2(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,3])
        self.assertEqual(True, a <= b)

    def test_not_less_or_equal(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,4,3])
        self.assertEqual(False, b <= a)

    def test_greater_or_equal(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([10,2,3])
        self.assertEqual(True, b >= a)

    def test_greater_or_equal2(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,2,3])
        self.assertEqual(True, b >= a)

    def test_not_greater_or_equal(self):
        a = DoubleLinkedList([1,2,3])
        b = DoubleLinkedList([1,4,3])
        self.assertEqual(False, a >= b)

    def test_slow_sort(self):
        a = DoubleLinkedList([5,4,7,6,8,3,4,1])
        a.slow_sort()
        self.assertEqual([1, 3, 4, 4, 5, 6, 7, 8], a.to_list())

    def test_slow_sort2(self):
        a = DoubleLinkedList()
        a.slow_sort()
        self.assertEqual([], a.to_list())

    def test_slow_sort3(self):
        a = DoubleLinkedList([1])
        a.slow_sort()
        self.assertEqual([1], a.to_list())

    def test_slow_sort4(self):
        a = DoubleLinkedList([1,2,3, 8, 7])
        a.slow_sort()
        self.assertEqual([1,2,3,7,8], a.to_list())

    def test_slow_sort5(self):
        a = DoubleLinkedList([1,2])
        a.slow_sort()
        self.assertEqual([1,2], a.to_list())

    def test_slow_sort6(self):
        a = DoubleLinkedList([2,1])
        a.slow_sort()
        self.assertEqual([1,2], a.to_list())

    def test_sort(self):
        a = DoubleLinkedList([5,4,7,6,8,3,4,1])
        a.sort()
        self.assertEqual([1, 3, 4, 4, 5, 6, 7, 8], a.to_list())

    def test_sort2(self):
        a = DoubleLinkedList()
        a.sort()
        self.assertEqual([], a.to_list())

    def test_sort3(self):
        a = DoubleLinkedList([1])
        a.sort()
        self.assertEqual([1], a.to_list())

    def test_sort4(self):
        a = DoubleLinkedList([1, 2, 3, 8, 7])
        a.sort()
        self.assertEqual([1, 2, 3, 7, 8], a.to_list())

    def test_sort5(self):
        a = DoubleLinkedList([1, 2])
        a.sort()
        self.assertEqual([1, 2], a.to_list())

    def test_sort6(self):
        a = DoubleLinkedList([2, 1])
        a.sort()
        self.assertEqual([1, 2], a.to_list())


class TestLinkedQueue(TestCase):
    def test_enqueue(self):
        a = LinkedQueue()
        a.enqueue(1)
        self.assertEqual([1], a._list.to_list())

    def test_dequeue(self):
        a = LinkedQueue()
        a.enqueue(1)
        b = a.dequeue()
        self.assertEqual(1, b)

    def test_dequeue2(self):
        a = LinkedQueue()
        a.enqueue(1)
        b = a.dequeue()
        self.assertEqual([], a._list.to_list())

    def test_len(self):
        a = LinkedQueue()
        a.enqueue(1)
        a.enqueue(2)
        a.enqueue(3)
        self.assertEqual(3, len(a))

    def test_enqueue_dequeue(self):
        a = LinkedQueue()
        a.enqueue(1)
        a.enqueue(2)
        b = a.dequeue()
        self.assertEqual(1, b)

    def test_is_empty(self):
        a = LinkedQueue()
        a.enqueue(1)
        a.enqueue(2)
        a.dequeue()
        a.dequeue()
        self.assertEqual(True, a.is_empty())


class TestLinkedStack(TestCase):
    def test_push(self):
        a = LinkedStack()
        a.push(1)
        self.assertEqual([1], a._list.to_list())

    def test_pop(self):
        a = LinkedStack()
        a.push(1)
        b = a.pop()
        self.assertEqual(1, b)

    def test_pop2(self):
        a = LinkedStack()
        a.push(1)
        b = a.pop()
        self.assertEqual([], a._list.to_list())

    def test_len(self):
        a = LinkedStack()
        a.push(1)
        a.push(2)
        a.push(3)
        self.assertEqual(3, len(a))

    def test_push_pop(self):
        a = LinkedStack()
        a.push(1)
        a.push(2)
        b = a.pop()
        self.assertEqual(2, b)

    def test_is_empty(self):
        a = LinkedStack()
        a.push(1)
        a.push(2)
        a.pop()
        a.pop()
        self.assertEqual(True, a.is_empty())


if __name__ == "__main__":
    unittest.main()