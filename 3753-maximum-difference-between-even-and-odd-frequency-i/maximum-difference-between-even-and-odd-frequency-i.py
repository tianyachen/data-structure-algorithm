class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        maxOdd = 0
        minEven = float("inf")

        for freq in counter.values():
            if freq % 2 == 0:
                minEven = min(minEven, freq)
            else:
                maxOdd = max(maxOdd, freq)

        return maxOdd - minEven