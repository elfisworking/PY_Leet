// 面试题 16.11. 跳水板
// https://leetcode-cn.com/problems/diving-board-lcci/
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
@File : 16.11.cpp
@Time : 2022/04/01 11:12:22
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> divingBoard(int shorter, int longer, int k) {
        vector<int> ans;
        if(k == 0) return ans;
        int minVal = shorter * k;
        int maxVal = longer * k;
        int sub = longer - shorter;
        if(sub == 0) {
            ans.emplace_back(minVal);
            return ans;
        }
        for(int i = minVal; i <= maxVal; i += sub) {
            ans.emplace_back(i);
        }
        return ans;
    }
};