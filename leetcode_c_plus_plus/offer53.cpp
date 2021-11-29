// 剑指 Offer 53 - II. 0～n-1中缺失的数字
// https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer53.cpp
@Time : 2021/11/29 15:53:09
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int a = accumulate(nums.begin(), nums.end(), 0);
        int l = nums.size();
        int b = l * (l + 1) / 2;
        return b - a; 
    }
};