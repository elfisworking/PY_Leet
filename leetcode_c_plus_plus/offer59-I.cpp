// 剑指 Offer 59 - I. 滑动窗口的最大值
// https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
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
@File : offer59-I.cpp
@Time : 2021/12/22 17:18:05
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> d;
        for(int i = 0; i < k; i++){
            while(!d.empty() && d.back() < nums[i]) d.pop_back();
            d.push_back(nums[i]);
        }
        int left = 0;
        vector<int> ans;
        for(int i = k; i < nums.size(); i++) {
            ans.push_back(d.front());
            if(nums[left] == d.front()) d.pop_front();
            left++;
            while(!d.empty() && d.back() < nums[i]) d.pop_back();
            d.push_back(nums[i]);
        }
        if(!d.empty()) ans.push_back(d.front());
        return ans;

    }
};