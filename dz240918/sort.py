def quick_sort[t](a: list[t]) -> list[t]:
    if len(a) <= 1:  # пустой список
        return a
    else:
        opora: int = a[len(a) // 2]  # опорный элемент
        #aver: int = a[opora]  # ср. значение списка исходя из опорного элемента(допустим 1,2,3,4,5) опора это 3
        minimum: list[int] = []  # тоже что и в maximum, но замените maximum на minimum
        maximum: list[int] = []  # максимальное значение(пока что неопред. в цикле определяется)
        ravnost: list[int] = []  # центральныый элемент
        for x in a:
            if x == opora:
                ravnost.append(x)
            elif x < opora:
                maximum.append(x)
            elif x > opora:
                minimum.append(x)
        return quick_sort(maximum) + ravnost + quick_sort(minimum)  # возвращаем все элементы включая опорный


if __name__ == "__main__":
    a: list[int] = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 21, -3, 384783]
    print(quick_sort(a))
    b: list[str] = ['a', 'h', 'r', 'b', 's', 'п', 'а']
    print(quick_sort(b))
