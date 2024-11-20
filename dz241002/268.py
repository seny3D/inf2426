#https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=EASY
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        def bin_search(nums: list[int], target: int) -> bool:
            l: int = 0
            r: int = len(nums)
            while r - l > 0:
                d: int = (r + l) // 2
                if nums[d] == target:
                    return True
                if target > nums[d]:
                    l = d + 1
                else:
                    r = d
            return False

        dlina: int = len(nums)
        nums.sort()
        vsp_arr: list[int] = [i for i in range(dlina + 1)]
        for i in vsp_arr:
            if not bin_search(nums, i):
                return i
