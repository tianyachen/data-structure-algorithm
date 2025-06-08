class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        unordered_set<char> row1 = {'q','w','e','r','t','y','u','i','o','p'};
        unordered_set<char> row2 = {'a','s','d','f','g','h','j','k','l'};
        unordered_set<char> row3 = {'z','x','c','v','b','n','m'};
        vector<string> ans;
        for(int i=0;i<words.size();i++){
            string low="";
            string word=words[i];
            for(int j=0;j<word.size();j++){
                char ch=word[j];
                low+=tolower(ch);
            }
            std::cout << low << endl;
            bool A=true ,B=true, C=true;
            for(int j=0;j<low.size();j++){
                if(row1.count(low[j])==NULL){
                    A=false;
                }
                if(row2.count(low[j])==NULL){
                    B=false;
                }
                if(row3.count(low[j])==NULL){
                    C=false;
                }
            }
            std::cout << A << " " << B << " " << C << endl;
            if(A || B || C){
                ans.push_back(words[i]);
            }
        }
        return ans;
    }
};