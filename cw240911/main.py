# вывести n первых чисел фиббоначи
a = int(input())
def fib(a: int):
    if a in (1,2):
        return 1
    return fib(a - 1) + fib(a - 2)
print(fib(a))
