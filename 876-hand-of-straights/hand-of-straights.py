class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(groupSize):
                current = first + i
                if count[current] == 0:
                    return False
                count[current] -= 1
                if count[current] == 0:
                    if current != minHeap[0]:
                        return False
                    
                    heapq.heappop(minHeap)
        
        return True
