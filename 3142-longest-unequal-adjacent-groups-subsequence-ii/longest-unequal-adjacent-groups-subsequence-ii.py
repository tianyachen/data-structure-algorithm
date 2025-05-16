class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        maxIndex = 0

        for i in range(1, n):
            for j in range(i):
                if self.hammingDist(words[i], words[j]) and dp[j] + 1 > dp[i] and groups[i] != groups[j]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxIndex]:
                maxIndex = i

        
        ans = []
        i = maxIndex
        while i >= 0:
            ans.append(words[i])
            i = prev[i]

        return ans[::-1]

    def hammingDist(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        diff = 0

        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        
        return diff == 1
