class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1

        return j == len(s)
        