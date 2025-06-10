class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxCount = 0

        for key, value in counter.items():
            if key + 1 in counter:
                maxCount = max(maxCount, counter[key + 1] + value)

        return maxCount