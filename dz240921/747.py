class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_: int = 0
        f: bool = False
        index_: int = 0
        for i in range(len(nums)):
            if nums[i] > max_:
                if max_ * 2 <= nums[i]:
                    f = True
                else:
                    f = False
                max_ = nums[i]
                index_ = i
                continue
            if f and max_ >= 2 * nums[i]:
                f = True
            else:
                f = False
        if f:
            return index_
        return -1
                
