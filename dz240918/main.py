from sort import quick_sort
from corob import Corob

if __name__ == "__main__":
    a: list[Corob] = [
        Corob(19, 19),
        Corob(10, 10),
        Corob(25, 50),
        Corob(5, 2),
        Corob(26, 51),
        Corob(7, 8),
        Corob(3,6),
        Corob(45, 20),
        Corob(44.98, 19.98),
    ]
    print(quick_sort(a))