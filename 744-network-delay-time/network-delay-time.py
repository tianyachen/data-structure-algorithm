class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = {}
        adj_list = defaultdict(list)

        for triplet in times:
            src, dest, time = triplet
            adj_list[src].append((dest, time))
        
        minHeap = [(0, k)]

        while minHeap:
            time, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            
            visited[src] = time

            for neighbor, t in adj_list[src]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (t + time, neighbor))

        if len(visited) == n:
            return max(visited.values())

        return -1 
