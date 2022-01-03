// 474. 一和零
// https://leetcode-cn.com/problems/ones-and-zeroes/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 474.cpp
@Time : 2022/01/02 20:08:51
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int length = strs.size();
        vector<vector<vector<int>>> dp(length + 1, vector<vector<int>>(m + 1, vector<int>(n + 1)));
        vector<pair<int, int>> nums;
        int count_m;
        int count_n;
        for(string str : strs) {
            count_n = 0;
            count_m = 0;
            for(char ch : str){
                if(ch == '0') count_m++;
                else count_n++;
            }
            nums.push_back(make_pair(count_m, count_n));
        }
        for(int i = 1; i <= length; i++) {
            for(int j = 0; j <= m; j++) {
                for(int k = 0; k <= n; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];
                    if(j >= nums[i - 1].first && k >= nums[i - 1].second) {
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - nums[i -1].first][k - nums[i - 1].second] + 1);
                    }
                }

            }
        }
        return dp[length][m][n];

    }
};