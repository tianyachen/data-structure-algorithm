class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), k in zip(equations, values):
            graph[a].append((b, k))
            graph[b].append((a, 1/k))


        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = set([start])

            while queue:
                node, value = queue.popleft()
                if node == end:
                    return value

                for nei, weight in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, value * weight))

            return -1.0

        return [bfs(a, b) for a, b in queries]