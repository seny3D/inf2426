def findShortestSubArray(nums: list[int]) -> int:
    d: dict = dict()
    pow: int = 0
    x: int = 0
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
            if pow < d[nums[i]]:
                pow = d[nums[i]]
                x = nums[i]
    if pow == 0:
        return 1
    l: int = 0
    r: int = len(nums) - 1
    f1: bool = False
    f2: bool = False
    while r > l and (not f1 or not f2):
        if nums[l] != x:
            l += 1
        else:
            f1 = True
        if nums[r] != x:
            r -= 1
        else:
            f2 = True
    return r - l + 1


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(findShortestSubArray(nums))
