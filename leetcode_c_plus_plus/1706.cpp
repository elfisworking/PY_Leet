// 1706. 球会落何处
// https://leetcode-cn.com/problems/where-will-the-ball-fall/
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
@File : 1706.cpp
@Time : 2022/02/24 23:31:09
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int n = grid[0].size();
        vector<int> ans(n);
        for(int j = 0; j < n; j++) {
            int col = j;
            for(auto &row : grid) {
                int dir = row[col];
                col += dir;
                if(col < 0 || col == n || row[col] != dir) {
                    col = -1;
                    break;
                }
            }
            ans[j] = col;
        }
        return ans;

    }
};