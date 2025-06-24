class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n + 1)]

        for triplet in times:
            src, dest, time = triplet
            adj_list[src].append((dest, time))
        
        minHeap = [(0, k)]
        shortest = [float('inf')] * (n + 1)
        shortest[k] = 0

        while minHeap:
            time, src = heapq.heappop(minHeap)
            if shortest[src] < time:
                continue

            for neighbor, t in adj_list[src]:
                if shortest[neighbor] > shortest[src] + t:
                    shortest[neighbor] = shortest[src] + t
                    heapq.heappush(minHeap, (t + time, neighbor))

        ans = max(shortest[1:])
        if ans == float('inf'):
            return -1

        return ans
