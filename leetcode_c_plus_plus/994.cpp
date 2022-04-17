// 994. 腐烂的橘子
// https://leetcode-cn.com/problems/rotting-oranges/
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
@File : 994.cpp
@Time : 2022/04/07 10:13:38
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int dirs[4][2] = {{1,0}, {-1, 0}, {0, 1}, {0, -1}};
        int m = grid.size(), n = grid[0].size();
        int ans = 0;

        while(ans < m * n) {
            vector<pair<int,int>> tmp;
            for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                    if(grid[i][j] == 2) {
                        for(auto & dir : dirs) {
                            int a = i + dir[0];
                            int b = j + dir[1];
                            if(a >= 0 && a < m && b >= 0 && b < n && grid[a][b] == 1) {
                                tmp.push_back(pair<int,int>{a, b});
                            }
                        }
                    }
                }
            }
            if(tmp.size() == 0) {
                break;
            }
            for(auto& orange : tmp) {
                grid[orange.first][orange.second] = 2;
            }
            ans++;
        }
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    return -1;
                }
            }
        }
        return ans;
    }
};