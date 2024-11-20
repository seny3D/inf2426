def sortbubble(sortir: list[int]) -> list[int]:
    for i in range(len(sortir) - 1, -1, -1):
        for k in range(i):
            if sortir[k + 1] < sortir[k]:
                sortir[k], sortir[k + 1] = sortir[k + 1], sortir[k]
    return sortir


def majorityElement(a: list[int]) -> int:
    if len(a) == 0:
        return 0
    else:
        sortbubble(a)
        x: int = len(a)
        greatcifra: int = a[x // 2]
        return greatcifra


if __name__ == '__main__':
    a = [3, 2, 3]
    print(majorityElement(a))
