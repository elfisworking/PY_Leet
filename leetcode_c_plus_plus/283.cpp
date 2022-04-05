// 283. 移动零
// https://leetcode-cn.com/problems/move-zeroes/
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
@File : 283.cpp
@Time : 2022/03/31 22:30:38
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = -1;
        for(int j = 0; j < nums.size(); j++) {
            if(nums[j] != 0) {
                i++;
                swap(nums[i], nums[j]);
            }
        }
    }
};