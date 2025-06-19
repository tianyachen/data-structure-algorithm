class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if (i, j) in visited:
                return 0

            visited.add((i, j))
            count = 1
            for dr, dc in directions:
                count += dfs(i + dr, j + dc)

            return count
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea