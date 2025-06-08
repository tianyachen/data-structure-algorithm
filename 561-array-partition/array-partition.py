class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                ans += num

        return ans