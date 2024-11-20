def sum_list(a: list[int]) -> int|None:
    if len(a):
        s: int = 0
        for el in a:
            s += el
        return s
    else:
        return None
    
    
if __name__ == "__main__":

    
    print(sum_list([1,2,3]))