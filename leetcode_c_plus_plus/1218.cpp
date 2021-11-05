class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int, int> dp;
        int ans = 0;
        for(auto i : arr) {
            dp[i] = dp[i -difference] + 1;
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};