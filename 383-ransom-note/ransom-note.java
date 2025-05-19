class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> freq = new HashMap<>();

        for (char c : magazine.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        for (char c : ransomNote.toCharArray()) {
            int curVal = freq.getOrDefault(c, 0) - 1;
            if (curVal < 0) {
                return false;
            }
            freq.put(c, curVal);
        }
        return true;
    }
}