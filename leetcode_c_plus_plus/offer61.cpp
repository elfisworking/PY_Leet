// 剑指 Offer 61. 扑克牌中的顺子
// https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer61.cpp
@Time : 2021/12/12 20:35:16
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        bool ans = true;
        int zero = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == 0) zero++;
            if(i > 0 && nums[i - 1] + 1 != nums[i] && nums[i - 1] != 0) {
                if(nums[i - 1] == nums[i]) return false;
                int sub = nums[i] - nums[i - 1] - 1;
                if(sub > zero) return false;
                else {
                    zero -= sub;
                }
            }
        }
        return ans;

    }
};