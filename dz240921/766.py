class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        elementzero: int = None
        for x in matrix:
            if elementzero != None:
                for i in range(1, len(x)):
                    if elementzero[i - 1] != x[i]:
                        return False
            elementzero = x
        return True
