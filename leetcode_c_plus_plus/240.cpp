// 240. 搜索二维矩阵 II
// https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
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
@File : 240.cpp
@Time : 2022/01/09 21:53:58
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        int col = matrix[0].size();
        int a = 0, b = col - 1;
        while(a < row && b >= 0) {
            if(matrix[a][b] < target) {
                a++;
            }else if(matrix[a][b] > target) {
                b--;
            }else {
                return true;
            }
        }
        return false;

        
    }
};