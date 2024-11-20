from bisect import bisect_left
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        oporapovorota: int = bisect_left(nums, 1, key=lambda x: 0 if x > nums[-1] else 1)
        '''
        опора точки смещения, где nums[-1] ласт элемент получаем что то типо [0,0,0,1,1]
        '''

        llist: list[int] = []
        rlist: list[int] = []
        # пока левый и правый лист пустые, удивительно, как же его заполнить.. Павел Георгиевич спасибо за подсказку с левым и правым

        for i in range(len(nums)):
            if i < oporapovorota:
                llist.append(nums[i])
            else:
                rlist.append(nums[i])

        # это было тяжело, я еле это вспомнил.


        li: int = bisect_left(llist, target)
        ri: int = bisect_left(rlist, target)
        # индксы лево право

        if ri < len(rlist) and rlist[ri] == target: # зря чтоли индексы объявляли? вот решение
            return oporapovorota + ri
        elif li < len(llist) and llist[li] == target:
            return li

        return -1