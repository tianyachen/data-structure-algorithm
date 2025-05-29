class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        start = 0
        ans = []

        for end in range(n):
            if end == n - 1 or (nums[end] + 1 != nums[end + 1]):
                if start == end:
                    ans.append(str(nums[end]))
                else:
                    ans.append("".join([str(nums[start]), "->", str(nums[end])]))
                start = end + 1
        
        return ans
