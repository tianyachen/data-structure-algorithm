class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for frm, to in tickets:
            heapq.heappush(graph[frm], to)

        ans = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                next_stop = heapq.heappop(graph[airport])
                dfs(next_stop)
            
            ans.append(airport)
        
        dfs("JFK")
        return ans[::-1]