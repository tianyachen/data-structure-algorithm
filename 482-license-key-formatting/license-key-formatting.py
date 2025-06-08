class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        countChar = 0

        for c in s:
            if c != '-':
                countChar += 1

        firstPartLen = countChar % k
        ans = []

        i = 0
        count = k

        while firstPartLen > 0 and i < len(s):
            if s[i] != '-':
                ans.append(s[i].upper())
                firstPartLen -= 1
            i += 1

        if i > 0 and i < len(s):
            ans.append('-')

        while i < len(s):
            if s[i] != '-':
                if count == 0:
                    ans.append('-')
                    count = k
                ans.append(s[i].upper())
                count -= 1
            
            i += 1
       
        return "".join(ans)