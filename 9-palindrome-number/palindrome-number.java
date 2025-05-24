class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int n = countNumOfDigits(x);
        int copy = x;
        int reversedNum = 0; 
        while (n > 0) {
            int digit = copy % 10;
            reversedNum += (int) Math.pow(10, n-1) * digit;
            copy /= 10; 
            n--;
        }
        return x == reversedNum;
    }

    private int countNumOfDigits(int x) {
        int n = 0;
        while (x != 0) {
            n++;
            x /= 10;
        }
        return n;
    }
}