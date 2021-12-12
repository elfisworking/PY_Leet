// 剑指 Offer 57. 和为s的两个数字
// https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
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
@File : offer57.cpp
@Time : 2021/12/10 14:16:31
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int left = 0, right = nums.size() - 1;
        while(left < right) {
            int n = nums[left] + nums[right];
            if(n == target) {
                ans.push_back(nums[left]);
                ans.push_back(nums[right]);
                return ans;
            } else if( n > target) right--;
            else left++;
        }
        return ans;

    }
};