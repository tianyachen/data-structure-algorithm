class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        visited = {}

        for flight in flights:
            u, v, w = flight
            adj_list[u].append((v, w))

        minHeap = [(0, src, 0)]

        while minHeap:
            price, node, stops = heapq.heappop(minHeap)
            if node == dst:
                return price
            
            if stops > k:
                continue

            if node in visited and stops >= visited[node]:
                continue
            
            visited[node] = stops

            for neighbor, nextPrice in adj_list[node]:
                heapq.heappush(minHeap, (price + nextPrice, neighbor, stops + 1))
        
        return -1