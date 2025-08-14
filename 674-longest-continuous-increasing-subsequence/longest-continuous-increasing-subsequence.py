class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        longestLen = 1
        cur = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur += 1
                longestLen = max(cur, longestLen)
            else:
                cur = 1

        return longestLen