// 64. 最小路径和
// https://leetcode-cn.com/problems/minimum-path-sum/
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
@File : 64.cpp
@Time : 2022/04/03 16:16:57
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(i > 0 && j > 0) {
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
                } else if(i == 0 && j > 0) {
                    grid[i][j] += grid[i][j - 1];
                } else if(j == 0 && i > 0) {
                    grid[i][j] += grid[i - 1][j];
                }
            }
        }
        return grid[row - 1][col - 1];

    }
};