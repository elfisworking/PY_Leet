// 34. 在排序数组中查找元素的第一个和最后一个位置
// https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
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
@File : 34.cpp
@Time : 2022/01/09 21:59:30
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking :
@Tag : Medium
class Solution {
**/
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.size() == 0) return vector<int>{-1, -1};
        int left = 0, right = nums.size();
        if(nums[right - 1] < target) return vector<int>{-1, -1};
        if(target < nums[left]) return vector<int>{-1, -1};
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] >= target) right = mid;
            else left = mid + 1;
        }
        int start = left;
        if(start < 0 || nums[start] != target) start = -1;
        left = 0;
        right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] > target) right = mid;
            else left = mid + 1;
        }
        int end = left - 1;
        if(end < 0 || nums[end] != target) end = -1;
        return vector<int>{start, end};

    }
};