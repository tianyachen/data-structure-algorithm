class Solution {
    int BASE26 = 26;
    public String convertToTitle(int columnNumber) {
        StringBuilder ans = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--;
            ans.append((char) (columnNumber % BASE26 + 'A'));
            columnNumber /= BASE26;
        }
        return ans.reverse().toString();
    }
}