class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        ans = []
        for key in count1.keys():
            if key in count2:
                time = min(count1[key], count2[key])
                while time > 0:
                    ans.append(key)
                    time -= 1

        return ans