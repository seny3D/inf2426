# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# https://leetcode.com/problems/flatten-nested-list-iterator/?envType=problem-list-v2&envId=iterator
class NestedInteger:
    def isInteger(self) -> bool:
        ...

    def getInteger(self) -> int:
        ...

    def getList(self) -> [NestedInteger]:
        ...


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack: [NestedInteger] = []
        self._add(nestedList)

    def _add(self, nestedList) -> Self:
        for x in reversed(nestedList):
            self.stack.append(x)

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            full = self.stack[-1]
            if full.isInteger():
                return True
            self.stack.pop()
            self._add(full.getList())
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())