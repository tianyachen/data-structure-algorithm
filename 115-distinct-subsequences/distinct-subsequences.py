class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        memo = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if j == n:
                return 1
            if i == m:
                return 0

            count = 0

            if s[i] == t[j]:
                count += dfs(i + 1, j + 1)
            
            count += dfs(i + 1, j)

            memo[(i, j)] = count
            return memo[(i, j)]

        return dfs(i = 0, j = 0)