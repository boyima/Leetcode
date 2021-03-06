class Solution {
public:
    int numDecodings(string s) {
        if(!isdigit(s[0]) || s[0] == '0'){
            return 0;
        }
        vector<int> dp(s.size() + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 1; i < s.size(); i++){
            if(!isdigit(s[i])) return 0;
            int v = 10 * (s[i - 1] - '0') + (s[i] - '0');
            if(v > 9 && v <= 26){
                dp[i + 1] = dp[i + 1] + dp[i - 1];
            }
            if(s[i] != '0'){
                dp[i + 1] = dp[i + 1] + dp[i];
            }
        }
        return dp[s.size()];
    }
};
