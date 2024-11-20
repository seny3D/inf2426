class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        check: int = 0
        if len(bits) == 1:
            return 1 + 1 == 2
        else:
            while check < len(bits) - 1:
                if bits[check] != 0:
                    check += 2
                elif bits[check] == 0:
                    check += 1
                else:
                    check += 0
            return len(bits) != check