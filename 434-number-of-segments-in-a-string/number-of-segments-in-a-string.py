class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i != len(s):
            count += 1
        
        while i < len(s):
            if s[i] == ' ' and i + 1 < len(s) and s[i + 1] != ' ':
                count += 1
            i += 1
            

        return count

        