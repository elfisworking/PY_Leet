// 35. 搜索插入位置
// https://leetcode-cn.com/problems/search-insert-position/
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
@File : 35.cpp
@Time : 2021/12/15 10:25:18
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] >=  target) right = mid;
            else left = mid + 1;
        }
        return right;

    }
};

