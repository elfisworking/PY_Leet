// 221. 最大正方形
// https://leetcode-cn.com/problems/maximal-square/
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
@File : 221.cpp
@Time : 2022/03/26 15:30:54
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        if(row == 0 || col == 0) return 0;
        int ans = 0;
        vector<vector<int>> dp(row, vector<int>(col, 0));
        for(int i = 0; i < col; i++) {
            if(matrix[0][i] == '1') {
                dp[0][i]= 1;
                ans = 1;
            }
        }
        for(int i = 0; i < row; i++)  {
            if(matrix[i][0] == '1') {
                dp[i][0] = 1;
                ans = 1;
            }
        }
        for(int i = 1; i < row; i++) {
            for(int j = 1; j < col; j++) {
                if(matrix[i][j] == '0') continue;
                dp[i][j] = min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]}) + 1;
                ans = max(ans, dp[i][j]);
            }
        }
        return ans * ans;
        

    }
};