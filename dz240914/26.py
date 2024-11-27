#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array&difficulty=EASY
class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        i: int = 1
        for x in range(1, len(a)):
            if a[x] != a[x - 1]:
                a[i] = a[x]
                i += 1
        return i
