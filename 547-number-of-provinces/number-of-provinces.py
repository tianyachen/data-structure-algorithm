class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        n = len(isConnected)
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                queue = deque([i])
                seen.add(i)
                while queue:
                    node = queue.popleft()
                    for j in range(n):
                        if isConnected[node][j] == 1 and j not in seen:
                            queue.append(j)
                            seen.add(j)

        return count
                    