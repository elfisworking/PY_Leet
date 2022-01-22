// 剑指 Offer 61. 扑克牌中的顺子
// https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_set>
#include<unordered_map>
#include<limits>
using namespace std;
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
class Solution {
public:
    bool isStraight(vector<int>& nums) {
        if(nums.size() != 5) return false;
        unordered_set<int> set;
        int minVal = 14, maxVal = 0;
        for(int x: nums) {
            if(set.count(x) != 0) return false;
            minVal = min(minVal, x);       
            maxVal = max(maxVal, x); 
        }
        return maxVal - minVal < 5 ? true : false;
        
    }
};