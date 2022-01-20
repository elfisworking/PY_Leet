// 540. 有序数组中的单一元素
// https://leetcode-cn.com/problems/single-element-in-a-sorted-array/
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
@File : 540.cpp
@Time : 2022/01/19 23:33:59
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(mid % 2 == 1) mid--;
            if(mid + 1 < nums.size() && nums[mid] == nums[mid + 1]) {
                left = mid + 2;
            } else {
                right = mid;
            }
        }
        return nums[left];

    }
};
