class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        ans = [-1] * len(queries)
        minHeap = []
        i = 0

        for query, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                if end >= query:
                    heapq.heappush(minHeap, (end - start + 1, end))
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            if minHeap:
                ans[idx] = minHeap[0][0]
            

        return ans