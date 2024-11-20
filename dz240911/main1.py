from __future__ import annotations


def fib(n: int) -> int:
    try:
        if n == 1 or n == 2:
            return 1
        ab = fib(n - 1) + fib(n - 2)
        return ab
    except TypeError:
        err = 'Вы ввели некоректные данные'
        return err
def sum_list(a: list[int]) -> int|None:
    try:
        if len(a) == 0:
            return None
        n:int = a[0]
        for x in range(1,len(a)):
            n = n + a[x]
        return n
    except TypeError:
        err = 'Вы ввели неккоректные данные'
        return err

def max_list(a: list[int]) -> int|None:
    g = 0
    if len(a) == 0:
        return None
    try:
        n:int = a[0]
        for x in range(1,len(a)):
            if a[x] > g:
                n = a[x]
        return n
    except TypeError:
        err = 'Вы ввели неккоректные данные'
        return err
def max_list2(a: list[int]) -> tuple|None:
    try:
        if len(a) == 0:
            return None, None
        if len(a) == 1:
            return a[0], None
        maximum:int = max_list(a)
        secmax: int
        for x in range(0,len(a)):
            if a[x] != maximum and maximum > a[x]:
                secmax = a[x]-1
            if secmax < a[x]:
                secmax = a[x]-1
        return maximum,secmax

    except TypeError:
        err = 'Вы ввели неккоректные данные'
        return err
    except UnboundLocalError:
        err = 'Вы ввели неккоректные данные'
        return err
def min_max_list(a: list[int]) -> tuple|None:
    try:
        if len(a) == 0:
            return None, None
        else:
            minimum: int = a[0]
            for x in range(1,len(a)):
                if minimum > a[x]:
                    minimum = a[x]
            return minimum, max_list(a)
    except TypeError:
        err = 'Вы ввели неккоректные данные'
        return err
def mean_list(a: list[int]) -> float|None:
    try:
        if len(a) == 0:
            return None
        return sum_list(a) / len(a)
    except TypeError:
        err = 'Вы ввели неккоректные данные'
        return err

def median_list(a: list[int]) -> float|None:
    try:
        a.sort()
        if len(a) == 0:
            return None
        if len(a) % 2 == 0:
            return a[len(a)//2] + a[len(a)//2-1]/2
        return a[(len(a)-1) // 2]
    except TypeError:
        err = 'Вы ввели неккоректные данные'
        return err

if __name__ == '__main__':
    a:list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    k:int = 10
    try:
        for x in range(1,k+1):
            print(fib(x))
    except TypeError:
        print('Вы ввели некорректные данные')
    print(sum_list(a))
    print(max_list(a))
    print(max_list2(a))
    print(min_max_list(a))
    print(mean_list(a))
    print(median_list(a))

