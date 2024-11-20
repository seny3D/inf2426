from unittest import TestCase, main

from bst import BST

# Метод setUp() вызывается перед каждым тестом и предназначен для подготовки прогона.
# Метод tearDown() вызывается после того, как тест был запущен и результат записан.
# Метод запускается даже в случае исключения в теле теста.


class TestBST(TestCase):
    def setUp(self):
        self.bst = BST()

    def test_from_list(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.assertEqual(6, len(self.bst))

    def test_search(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.assertEqual(True, self.bst.search(5))

    def test_search2(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.assertEqual(False, self.bst.search(0))

    def test_insert(self):
        self.bst.insert(5)
        self.assertEqual(1, len(self.bst))

    def test_insert2(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(5)
        self.assertEqual(7, len(self.bst))

    def test_insert3(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(10)
        self.assertEqual(7, len(self.bst))

    def test_insert4(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(-10)
        self.assertEqual(7, len(self.bst))

    def test_insert5(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(5)
        self.bst.insert(5)
        self.assertEqual(8, len(self.bst))

    def test_insert6(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(10)
        self.bst.insert(-1)
        self.assertEqual(8, len(self.bst))

    def test_insert7(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(10)
        self.assertEqual(True, self.bst.search(10))

    def test_insert8(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(10)
        self.assertEqual(True, self.bst.search(1))

    def test_insert9(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(10)
        self.assertEqual(False, self.bst.search(-1))

    def test_insert10(self):
        self.bst.from_list([1,2,3,4,5,6])
        self.bst.insert(-1)
        self.bst.insert(10)
        self.assertEqual(True, self.bst.search(-1))

    def test_delete(self):
        self.bst.delete(5)
        self.assertEqual(0, len(self.bst))

    def test_delete2(self):
        self.bst.insert(5)
        self.bst.delete(5)
        self.assertEqual(0, len(self.bst))

    def test_delete3(self):
        self.bst.insert(2)
        self.bst.delete(5)
        self.assertEqual(1, len(self.bst))

    def test_delete4(self):
        self.bst.insert(2)
        self.bst.delete(5)
        self.assertEqual(True, self.bst.search(2))

    def test_delete5(self):
        self.bst.insert(2)
        self.bst.delete(5)
        self.assertEqual(False, self.bst.search(5))

    def test_delete6(self):
        self.bst.from_list([1, 2, 3, 4, 5, 6])
        self.bst.delete(1)
        self.assertEqual(False, self.bst.search(1))

    def test_delete7(self):
        self.bst.from_list([1, 2, 3, 4, 5, 6])
        self.bst.delete(1)
        self.assertEqual(5, len(self.bst))

    def test_delete8(self):
        self.bst.from_list([1, 2, 3, 4, 5, 6])
        self.bst.delete(1)
        self.bst.delete(2)
        self.bst.delete(3)
        self.bst.delete(4)
        self.bst.delete(5)
        self.bst.delete(6)
        self.assertEqual(0, len(self.bst))

    def test_delete9(self):
        self.bst.from_list([1, 2, 3, 4, 5, 6])
        self.bst.delete(2)
        self.bst.delete(3)
        self.bst.delete(4)
        self.bst.delete(5)
        self.bst.delete(6)
        self.assertEqual(1, len(self.bst))

    def test_delete10(self):
        self.bst.from_list([1, 2, 3, 4, 5, 6])
        self.bst.delete(2)
        self.bst.delete(3)
        self.bst.delete(4)
        self.bst.delete(5)
        self.bst.delete(6)
        self.assertEqual(True, self.bst.search(1))

    def test_delete11(self):
        self.bst.insert(1)
        self.bst.delete(2)
        self.bst.insert(2)
        self.bst.delete(2)
        self.bst.insert(4)
        self.bst.delete(4)
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.delete(5)
        self.bst.delete(6)
        self.assertEqual(True, self.bst.search(1))

    def test_delete12(self):
        self.bst.insert(1)
        self.bst.delete(2)
        self.bst.insert(2)
        self.bst.delete(2)
        self.bst.insert(4)
        self.bst.delete(4)
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.delete(5)
        self.bst.delete(6)
        self.assertEqual(1, len(self.bst))

    def test_delete13(self):
        self.bst.insert(1)
        self.bst.delete(2)
        self.bst.insert(2)
        self.bst.delete(2)
        self.bst.insert(4)
        self.bst.delete(4)
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.delete(5)
        self.bst.delete(6)
        self.bst.delete(1)
        self.assertEqual(0, len(self.bst))

if __name__ == "__main__":
    main()
