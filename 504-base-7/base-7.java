class Solution {
    public String convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }
        StringBuilder res = new StringBuilder();
        boolean isNegative = (num < 0);
        num = Math.abs(num);

        while (num > 0) {
            res.append("" + (num % 7));
            num /= 7;
        }

        String ret = res.reverse().toString();
        return isNegative ? '-' + ret : ret;
    }
}