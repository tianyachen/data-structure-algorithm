class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        ans = []

        def dfs(r, c, visited, prevHeight) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if visited[r][c]:
                return
            if heights[r][c] < prevHeight:
                return
            visited[r][c] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n - 1, atlantic, heights[i][n - 1])

        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m - 1, j, atlantic, heights[m - 1][j])

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans