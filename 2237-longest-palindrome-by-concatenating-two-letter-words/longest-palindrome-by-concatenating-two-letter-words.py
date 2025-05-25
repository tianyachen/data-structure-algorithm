class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = 0
        wordsMap = defaultdict(int)
        centerUsed = False
        for word in words:
            reverse = word[::-1]
            if reverse in wordsMap and wordsMap[reverse] > 0:
                count += 2
                wordsMap[reverse] -= 1
            else :
                wordsMap[word] += 1
        
        for word in wordsMap:
            if word[0] == word[1] and wordsMap[word] > 0:
                centerUsed = True
                break

        return count * 2 + (2 if centerUsed else 0)