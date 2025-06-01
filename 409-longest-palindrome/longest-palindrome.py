class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterCount = Counter(s)
        ans = 0
        oddFound = False
        for value in letterCount.values():
            if value % 2 == 1:
                ans += value - 1
                oddFound = True
            else:
                ans += value 

        if oddFound:
            ans += 1
        return ans