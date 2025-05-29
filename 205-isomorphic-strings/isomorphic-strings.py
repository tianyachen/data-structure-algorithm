class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_map1 = {}
        letter_map2 = {}

        for char1, char2 in zip(s, t):
            diff1 = ord(char1) - ord(char2)
            diff2 = ord(char2) - ord(char1)
            if char1 not in letter_map1:
                letter_map1[char1] = diff1
            if char2 not in letter_map2:
                letter_map2[char2] = diff2
            if letter_map1[char1] != diff1 or letter_map2[char2] != diff2:
                return False
                

        return True
                