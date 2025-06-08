class Solution {
    public boolean checkPerfectNumber(int num) {
        int total = 0;
        for (int x = 1; x <= num / 2; x++) {
            if (num % x == 0) {
                total += x;
            }
        }
        return total == num;
    }
}