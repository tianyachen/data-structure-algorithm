class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> unique = new HashSet<Character>();
        int size = 0;
        int start = 0;
        for (int end = 0; end < s.length(); end++) {
            Character cur = s.charAt(end);
            while (unique.contains(cur)) {
                unique.remove(s.charAt(start));
                start++;
            }
            unique.add(cur);
            size = Math.max(size, end - start + 1);
        }

        return size;
    }
}