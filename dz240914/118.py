#https://leetcode.com/problems/pascals-triangle/?envType=problem-list-v2&envId=array&difficulty=EASY
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: list[list[int]] = []
        for x in range(numRows):
            row: list[int] = [1] * (x+1)
            for i in range(1, x):
                row[i]: list[int] = result[x-1][i-1] + result[x-1][i]
            result.append(row)
        return result