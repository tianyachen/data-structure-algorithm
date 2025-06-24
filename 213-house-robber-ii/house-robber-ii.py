class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(begin: int, end: int) -> int:
            prev1, prev2 = 0, 0

            for i in range(begin, end):
                curr = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = curr
            
            return curr
        
        return max(rob_line(0, len(nums) - 1), rob_line(1, len(nums)))
