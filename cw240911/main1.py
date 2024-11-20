glist = [1, 2, 3]
def sum_list(a: glist)-> int:
    s = 0
    len_list = len(glist)
    if len_list == 0:
        return None
    else:
        for x in range(len(glist)):
            a = a + glist[x]
            return a


if __name__ == "__main1__":
    print(sum_list([]))