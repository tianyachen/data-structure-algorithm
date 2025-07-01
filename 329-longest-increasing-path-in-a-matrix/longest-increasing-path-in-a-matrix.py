class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        @lru_cache(None)
        def dfs(i: int, j: int, prevNum: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if matrix[i][j] <= prevNum:
                return 0
            
            pathSize = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                pathSize = max(pathSize, 1 + dfs(i + dr, j + dc, matrix[i][j]))
            
            return pathSize
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        
        return ans