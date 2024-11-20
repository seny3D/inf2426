def containsDuplicate(a: list[int]) -> bool:
    n: int = len(set(a))
    k: int = len(a)
    if n != k:
        return True
    else:
        return False

if __name__ == "__main__":
    a = [1, 2, 3, 1]
    print(containsDuplicate(a))