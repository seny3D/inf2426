import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def srtUp(self):
        self.ll = LinkedList()

    def test_add_first(self):
        ll = LinkedList()
        ll.addfirst(5)
        self.assertEqual(ll._head.data, 5)

    def test_add_first2(self):
        ll = LinkedList()
        ll.addfirst(5)
        ll.addfirst(10)
        self.assertEqual((ll._head.data, ll._head.link.data), (10, 5))

    def test_add_last(self):
        ll = LinkedList()
        ll.addlast(5)
        self.assertEqual((ll._head.data, ll._head.link), (5, None))

    def test_remove_first(self):
        ll = LinkedList()
        ll.removefirst()
        self.assertEqual((ll._head.data, ll._head.link.data), (5, 10))

if __name__ == '__main__':
    unittest.main()