class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            if self.isSameRow(word):
                ans.append(word)

        return ans
        
    def isSameRow(self, word: str) -> bool:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        onlyFirst = onlySecond = onlyThird = True

        for c in word:
            if c.lower() not in first_row:
                onlyFirst = False
            if c.lower() not in second_row:
                onlySecond = False
            if c.lower() not in third_row:
                onlyThird = False
        return onlyFirst or onlySecond or onlyThird
            