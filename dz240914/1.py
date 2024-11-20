def removeDuplicates(a: list[int]) -> int:
    i: int = 1
    for x in range(1, len(a)):
        if a[x] != a[x - 1]:
            a[i] = a[x]
            i += 1
    return i


if __name__ == "__main__":
    a = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(a))
