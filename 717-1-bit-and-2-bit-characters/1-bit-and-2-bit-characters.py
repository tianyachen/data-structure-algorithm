class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n - 1:
            i += 2 if bits[i] == 1 else 1

        return i == n - 1
        
        