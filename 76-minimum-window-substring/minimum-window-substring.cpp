class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> map(128,0);
        for (char c: t) map[c]++;
        int counter= t.size(), begin = 0, end = 0, minLen= INT_MAX, minStart = 0;
        while(end < s.size()) {
            if (map[s[end]] > 0) counter--;
            map[s[end]]--;
            end++;
            while(counter==0) {
                if (end - begin < minLen) {
                    minStart = begin;
                    minLen = end - minStart;
                }
                if (map[s[begin]] == 0) {
                    counter++;
                }
                map[s[begin]]++;
                begin++;
            }
        }
        return minLen == INT_MAX?  "" : s.substr(minStart, minLen);
    }
};