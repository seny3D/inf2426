from typing import Optional, Any
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Any = left
        self.right: Any = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkup(number: Optional, low: int = (-2 ** 31 - 1),
        high: int = (1 + 2 ** 31)) -> bool:

            if number is None:
                return 1 == 1
            if number.val <= low:
                return 1 == 2

            elif number.val >= high:
                return 1 == 2

            return checkup(number.left, low, number.val) and checkup(number.right, number.val, high)

        return checkup(root)