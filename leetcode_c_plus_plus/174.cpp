// 174. 地下城游戏
// https://leetcode-cn.com/problems/dungeon-game/
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
@File : 174.cpp
@Time : 2022/04/05 22:45:09
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int n = dungeon.size(), m = dungeon[0].size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, INT_MAX));
        dp[n][m - 1] = dp[n - 1][m] = 1;
        for(int i = n -1; i >= 0; i--) {
            for(int j = m - 1; j >= 0; j--) {
                int minn = min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = max(minn - dungeon[i][j], 1);
            }
        }
        return dp[0][0];

    }
};

// class Solution {
// public:
//     int calculateMinimumHP(vector<vector<int>>& dungeon) {
//         int n = dungeon.size(), m = dungeon[0].size();
//         vector<vector<int>> dp(n + 1, vector<int>(m + 1, INT_MAX));
//         dp[n][m - 1] = dp[n - 1][m] = 1;
//         for (int i = n - 1; i >= 0; --i) {
//             for (int j = m - 1; j >= 0; --j) {
//                 int minn = min(dp[i + 1][j], dp[i][j + 1]);
//                 dp[i][j] = max(minn - dungeon[i][j], 1);
//             }
//         }
//         return dp[0][0];
//     }
// };
