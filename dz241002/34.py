#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=MEDIUM
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bin_left(a: list[int], target) -> int:
            l: int = -1
            r: int = len(a) - 1
            while r - l > 1:
                d: int  = (r + l) // 2
                if target <= a[d]:
                    r = d
                else:
                    l = d
            if len(a) < 1 or a[r] != target:
                return -1
            else:
                return r
        def bin_right(a: list[int], target) -> int:
            l: int = 0
            r: int = len(a)
            while r - l > 1:
                d: int  = (r + l) // 2
                if target >= a[d]:
                    l = d
                else:
                    r = d
            if len(a) < 1 or a[l] != target:
                return -1
            else:
                return l
        return [bin_left(nums, target) , bin_right(nums, target) ]