// 1909. 删除一个元素使数组严格递增
// https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
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
@File : 1909.cpp
@Time : 2022/04/02 22:16:10
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int l = nums.size();
        if(l <= 1) return true;
        int left = 0;
        int right = l - 1;
        while(left < l - 1) {
            if(nums[left] >= nums[left + 1]) break;
            left++;
        } 
        if(left == l - 1) return true;
        while(right > left) {
            if(nums[right] <= nums[right - 1]) break;
            right--;
        }
        if(right != left + 1) return false;
        if(left == 0 || nums[left - 1] < nums[right] ||right == l - 1 ||  nums[left] < nums[right + 1]) return true;
        return false;

    }
};
