// 189. 轮转数组
// https://leetcode-cn.com/problems/rotate-array/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
/**
@File : 189.cpp
@Time : 2021/11/09 23:12:52
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int s = nums.size();
        vector<int> tmp(nums.size());
        for(int i =0; i < nums.size(); i++) {
            int index = (i + k) % s;
            tmp[index] = nums[i];
        }
        nums.assign(tmp.begin(), tmp.end());

    }
};