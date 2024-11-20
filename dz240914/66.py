def plusOne(a: list[int]) -> list[int]:
    if len(a) == 0:
        return 0
    else:
        for x in range(len(a) - 1, -1, -1):
            if a[x] != 9:
                a[x] = a[x] + 1
                return a
            else:
                a[x] = 0
        itog = [1] + a
        return itog


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(plusOne(a))
