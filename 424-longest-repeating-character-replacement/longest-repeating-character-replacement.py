class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        count = [0] * 26
        max_count = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1
            max_count = max(max_count, count[index])

            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans

