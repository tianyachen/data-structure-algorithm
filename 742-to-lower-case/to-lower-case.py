class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []

        for c in s:
            if  'A' <= c <= 'Z':
                ans.append(chr(ord(c) + 32))
            else:
                ans.append(c)

        return "".join(ans)