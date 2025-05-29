class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(list(s))
        t_count = Counter(list(t))
        ans = ""
        for key in t_count.keys():
            if key not in s_count:
                ans = key
                break
            elif s_count[key] != t_count[key]:
                ans = key
                break
                

        return ans