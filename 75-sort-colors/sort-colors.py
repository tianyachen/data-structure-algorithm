class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            if num == 0:
                count[0] += 1
            elif num == 1:
                count[1] += 1
            else:
                count[2] += 1
        
        for i in range(len(nums)):
            if count[0] > 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] > 0:
                nums[i] = 1
                count[1] -= 1
            else:
                nums[i] = 2
                count[2] -= 1
        
        