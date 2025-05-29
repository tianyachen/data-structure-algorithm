class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans = 0;
        int exp = 0;
        reverse(columnTitle.begin(), columnTitle.end());
        for (char c : columnTitle) {
            ans += (int) (c - 'A' + 1) * pow(26, exp++);
        }
        return ans;
    }
};