// 470. 用 Rand7() 实现 Rand10()
// https://leetcode-cn.com/problems/implement-rand10-using-rand7/
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
@File : 470.cpp
@Time : 2022/01/08 17:20:08
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
**/
class Solution {
    int rand10() {
        int row, col, idx;
        do {
            row = rand7();
            col = rand7();
            idx = col + (row - 1) * 7;
        } while(idx > 40)
        return 1 + (idx - 1) % 10;
    }
};
