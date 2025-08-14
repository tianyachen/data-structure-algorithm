class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        curMax = float("-inf")
        secondMax = float("-inf")
        maxIndex = -1

        for i, num in enumerate(nums):
            if num > curMax:
                secondMax = curMax
                curMax = num
                maxIndex = i
            elif num > secondMax:
                secondMax = num

        return maxIndex if curMax >= secondMax * 2 else -1