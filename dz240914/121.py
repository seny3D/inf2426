def maxProfit(a: list[int]) -> int:
    if len(a) == 0:
        return 0

    minimum: int = 100000000
    maximum: int = 0
    for x in a:
        if x < minimum:
            minimum = x
        elif x - minimum > maximum:
            maximum = x - minimum

    return maximum


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    print(maxProfit(a))
