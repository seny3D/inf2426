from unittest import TestCase, main

from heap import Heap, HeapMin, QueueWithPriority


# Метод setUp() вызывается перед каждым тестом и предназначен для подготовки прогона.
# Метод tearDown() вызывается после того, как тест был запущен и результат записан.
# Метод запускается даже в случае исключения в теле теста.


class TestHeap(TestCase):
    def setUp(self):
        self.heap = Heap()

    def test__cmp(self):
        self.assertEqual(True, self.heap._cmp(5, 2) > 0)

    def test__cmp2(self):
        self.assertEqual(True, self.heap._cmp(2, 5) < 0)

    def test__cmp3(self):
        self.assertEqual(True, self.heap._cmp(2, 2) == 0)

    def test__cmp4(self):
        self.assertEqual(True, self.heap._cmp("abc", "bcd") < 0)

    def test_insert(self):
        self.heap.insert(5)
        self.assertEqual(1, len(self.heap))

    def test_insert2(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.assertEqual(2, len(self.heap))

    def test_get_max(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.assertEqual(10, self.heap.get_max())

    def test_get_max2(self):
        self.assertRaises(RuntimeError, self.heap.get_max)

    def test_extract_max(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.heap.extract_max()
        self.assertEqual(4, len(self.heap))

    def test_extract_max2(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.assertEqual(10, self.heap.extract_max())

    def test_extract_max3(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.heap.extract_max()
        self.assertEqual(6, self.heap.extract_max())

    def test_extract_max4(self):
        self.assertRaises(RuntimeError, self.heap.extract_max)


class TestHeapMin(TestCase):
    def setUp(self):
        self.heap = HeapMin()

    def test__cmp(self):
        self.assertEqual(True, self.heap._cmp(5, 2) < 0)

    def test__cmp2(self):
        self.assertEqual(True, self.heap._cmp(2, 5) > 0)

    def test__cmp3(self):
        self.assertEqual(True, self.heap._cmp(2, 2) == 0)

    def test__cmp4(self):
        self.assertEqual(True, self.heap._cmp("abc", "bcd") > 0)

    def test_insert(self):
        self.heap.insert(5)
        self.assertEqual(1, len(self.heap))

    def test_insert2(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.assertEqual(2, len(self.heap))

    def test_get_min(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.assertEqual(-10, self.heap.get_min())

    def test_get_min2(self):
        self.assertRaises(RuntimeError, self.heap.get_min)

    def test_extract_min(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.heap.extract_min()
        self.assertEqual(4, len(self.heap))

    def test_extract_min2(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.assertEqual(-10, self.heap.extract_min())

    def test_extract_min3(self):
        self.heap.insert(5)
        self.heap.insert(6)
        self.heap.insert(10)
        self.heap.insert(-10)
        self.heap.insert(2)
        self.heap.extract_min()
        self.assertEqual(2, self.heap.extract_min())

    def test_extract_min4(self):
        self.assertRaises(RuntimeError, self.heap.extract_min)


class TestQueueWithPriority(TestCase):
    def setUp(self):
        self.queue = QueueWithPriority()

    def test_enqueue(self):
        self.queue.enqueue(5, 2)
        self.assertEqual(1,  len(self.queue))

    def test_enqueue2(self):
        self.queue.enqueue(5, 2)
        self.queue.enqueue(6, 2)
        self.assertEqual(2,  len(self.queue))

    def test_enqueue3(self):
        self.queue.enqueue(5, 2)
        self.queue.enqueue(6, 1)
        self.assertEqual(2,  len(self.queue))

    def test_peek(self):
        self.queue.enqueue(5, 2)
        self.assertEqual(5,  self.queue.peek())

    def test_peek2(self):
        self.queue.enqueue(5, 2)
        self.queue.enqueue(6, 2)
        self.assertEqual(5,  self.queue.peek())

    def test_peek3(self):
        self.queue.enqueue(5, 2)
        self.queue.enqueue(6, 1)
        self.assertEqual(6,  self.queue.peek())

    def test_dequeue(self):
        self.assertRaises(RuntimeError, self.queue.dequeue)

    def test_dequeue2(self):
        self.queue.enqueue(5, 2)
        self.assertEqual(5, self.queue.dequeue())

    def test_dequeue3(self):
        self.queue.enqueue(5, 2)
        self.queue.dequeue()
        self.assertEqual(0, len(self.queue))

    def test_dequeue4(self):
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 2)
        self.assertEqual(6, self.queue.dequeue())

    def test_dequeue5(self):
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 1)
        self.assertEqual(5, self.queue.dequeue())

    def test_dequeue6(self):
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 1)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 1)
        self.queue.dequeue()
        self.assertEqual(8, self.queue.dequeue())

    def test_dequeue7(self):
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 1)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 1)
        self.queue.dequeue()
        self.assertEqual(3, len(self.queue))

    def test_dequeue8(self):
        self.queue.enqueue(10, 2)
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 2)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 2)
        self.assertEqual(10, self.queue.dequeue())

    def test_dequeue9(self):
        self.queue.enqueue(10, 2)
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 2)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 1)
        self.assertEqual(8, self.queue.dequeue())

    def test_dequeue10(self):
        self.queue.enqueue(10, 2)
        self.queue.enqueue(6, 2)
        self.queue.enqueue(5, 2)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 2)
        self.queue.dequeue()
        self.assertEqual(6, self.queue.dequeue())

    def test_dequeue11(self):
        self.queue.enqueue(10, 2)
        self.queue.enqueue(6, 1)
        self.queue.enqueue(5, 2)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 1)
        self.queue.dequeue()
        self.assertEqual(8, self.queue.dequeue())

    def test_empty(self):
        self.assertEqual(True, self.queue.empty())

    def test_empty2(self):
        self.queue.enqueue(10, 2)
        self.queue.enqueue(6, 1)
        self.queue.enqueue(5, 2)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 1)
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(True, self.queue.empty())

    def test_empty3(self):
        self.queue.enqueue(10, 2)
        self.queue.enqueue(6, 1)
        self.queue.enqueue(5, 2)
        self.queue.enqueue(7, 2)
        self.queue.enqueue(8, 1)
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(False, self.queue.empty())

if __name__ == "__main__":
    main()



