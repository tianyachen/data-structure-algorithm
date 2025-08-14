class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_index = {}
        last_index = {}
        count = {}

        for i, num in enumerate(nums):
            if num not in first_index:
                first_index[num] = i
            
            last_index[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        ans = float("inf")

        for num in nums:
            if count[num] == degree:
                ans = min(ans, last_index[num] - first_index[num] + 1)

        return ans
        