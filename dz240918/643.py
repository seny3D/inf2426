def findMaxAverage(nums: list[int]) -> float:
    summa = sum(nums[:k]) # общая сумма чисел
    donttouchsumma = summa # общая сумма которая не уч. в цикле
    for x in range(k, len(nums)): # цикл который проверяет массив от числа k(в сл. 1 примера это число 50)
        summa += nums[x] - nums[x - k]
        donttouchsumma = max(donttouchsumma, summa) # donttouchsumm проверяет максимальную сумму
    return donttouchsumma / k # вывод dts(donttou..) с проверкой на среднее число

a = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(a))
