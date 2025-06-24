class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            time, x, y = heapq.heappop(minHeap)
            if x == n - 1 and y == n - 1:
                return time

            if visited[x][y]:
                continue
            
            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                    newTime = max(time, grid[nx][ny])
                    heapq.heappush(minHeap, (newTime, nx, ny))