class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i_min: int = 0
        i_max: int = len(nums)

        while i_min < i_max:

            m: int = (i_max + i_min) // 2
            if target == nums[m]:
                return m

            if target > nums[m]:
                i_min = m + 1
            else:
                i_max = m

        if i_min >= len(nums):
            return len(nums)

        if i_max == 0:
            return 0
        return i_max
