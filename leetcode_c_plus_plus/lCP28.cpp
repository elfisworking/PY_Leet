// LCP 28. 采购方案
// https://leetcode-cn.com/problems/4xy4Wx/
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
@File : lCP28.cpp
@Time : 2022/04/03 16:00:01
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
#define MOD 1000000007
class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        for(int i = 1; i < nums.size(); i++) {
            int left_index = bisect(nums, i, target);
            if(left_index == -1) return ans;
            ans = (ans + left_index + 1) % MOD;
        }
        return ans;

    }

    int bisect(vector<int>& nums, int right_index, int target) {
        int right = right_index;
        int left = 0;
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[right_index] + nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left - 1;
    }
};
class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {
        int ans = 0;
        int left = 0;
        int right = nums.size() - 1;
        sort(nums.begin(), nums.end());
        while(left < right) {
            while(left < right && nums[left] + nums[right] > target) right--;
            ans = (ans + right - left) % 1000000007;
            left++;
        }
        return ans;
    }
};