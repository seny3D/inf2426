from typing import Self

class ListNode[T: object]:
    def __init__(self, data: T, link: Self|None = None, linkedlist: Self|None = None) -> None:
        self.data: T = data
        self.link: Self|None = link
        self.linkedlist: Self|None = linkedlist

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        item = self._tail.data
        self._tail.link = None
        if self._tail is None:
            self._head = None
        self._length -= 1
        return item

    # def removelast(self):
    #     if self._head is self._tail:
    #         return self.removefirst()
    #     else:
    #         currentnode = self._head
    #         while currentnode.link is not self._tail:
    #             currentnode = currentnode.link
    #         item = self._tail.data
    #         self._tail = currentnode
    #         self._tail.link = None
    #         self._length -= 1
    #         return item

    def __len__(self):
        return self._length

if __name__ == '__main__':
    LinkedList.removefirst()