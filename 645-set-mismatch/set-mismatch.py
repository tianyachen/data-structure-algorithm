class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        duplicate, missing = 0, 0

        for i in range(1, len(nums) + 1):
            if i in counter:
                if counter[i] == 2:
                    duplicate = i
            else:
                missing = i

        return [duplicate, missing]
