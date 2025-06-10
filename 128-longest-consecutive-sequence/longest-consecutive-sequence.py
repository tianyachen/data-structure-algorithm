class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        count = 0

        for num in nums:
            if num not in numMap:
                left = numMap.get(num - 1, 0)
                right = numMap.get(num + 1, 0)
                numMap[num] = left + right + 1
                numMap[num - left] = numMap[num]
                numMap[num + right] = numMap[num]
                count = max(count, numMap[num])
        return count
                

