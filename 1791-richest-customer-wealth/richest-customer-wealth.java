class Solution {
    public int maximumWealth(int[][] accounts) {
        int highestAmount = 0;
        int m = accounts.length;
        int n = accounts[0].length;

        for (int i = 0; i < m; i++) {
            int curAmount = 0;
            for (int j = 0; j < n; j++) {
                curAmount += accounts[i][j];
            }
            if (highestAmount < curAmount) {
                highestAmount = curAmount;
            }
        }
        return highestAmount;
    }
}