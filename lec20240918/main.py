def merge[T: int | str](m1: list[T], m2: list[T]) -> list[T]:
    res: list[T] = []
    i: int = 0
    j: int = 0
    while i < len(m1) and j < len(m2):
        if m1[i] <= m2[j]:
            res.append(m1[i])
            i += 1
        else:
            res.append(m2[j])
            j += 1

    while i < len(m1):
        res.append(m1[i])
        i += 1

    while j < len(m2):
        res.append(m2[j])
        j += 1

    return res


if __name__ == "__main__":
    print(merge([1,2,3], [2,3,4]))