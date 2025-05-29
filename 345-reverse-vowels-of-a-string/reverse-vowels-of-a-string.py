class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        vowel_pos = []

        for i in range(len(s_list)):
            if s_list[i] in vowels:
                vowel_pos.append(i)
        i = 0
        j = len(vowel_pos) - 1
        while i < j:
            s_list[vowel_pos[i]], s_list[vowel_pos[j]] = s_list[vowel_pos[j]], s_list[vowel_pos[i]]
            i += 1
            j -= 1

        return "".join(s_list)