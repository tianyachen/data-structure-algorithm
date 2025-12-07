class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxq = deque()
        n = len(nums)
        ans = []

        for i in range(n):
            while maxq and nums[i] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[i])
            
            if i - k >= 0 and nums[i - k] == maxq[0]:
                maxq.popleft()
            if i - k + 1 >= 0:
                ans.append(maxq[0])


        return ans