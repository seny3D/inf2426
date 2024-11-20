def findLengthOfLCIS(nums: list[int]) -> int:
    maxcount: int = 0
    count: int = 1
    for x in range(1, len(nums)):
        if nums[x] > nums[x - 1]:
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 1
    return max(maxcount, count)
