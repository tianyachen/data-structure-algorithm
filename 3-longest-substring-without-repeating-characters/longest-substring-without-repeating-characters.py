class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        i: int = 0
        j: int = 0
        max_window_size: int = 0
        window_chars: Set[str] = set()

        while j < len(s):
            if s[j] not in window_chars:
                window_chars.add(s[j])
                j += 1
            else:
                window_chars.remove(s[i])
                i += 1
            max_window_size = max(max_window_size, j - i)

        return max_window_size
        