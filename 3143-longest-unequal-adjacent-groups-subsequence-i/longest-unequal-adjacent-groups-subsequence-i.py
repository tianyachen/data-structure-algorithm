class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        indices = [0]

        for i in range(1, len(groups)):
            if groups[i] != groups[i - 1]:
                indices.append(i)

        return [words[i] for i in indices]