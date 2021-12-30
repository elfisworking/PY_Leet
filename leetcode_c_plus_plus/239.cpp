// 239. Sliding Window Maximum
// https://leetcode-cn.com/problems/sliding-window-maximum/
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
@File : 239.cpp
@Time : 2021/12/30 19:35:34
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking : 双端队列
@Tag : Hard
**/
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        for(int i = 0; i < k; i++) {
            while(!dq.empty() && dq.back() < nums[i]) dq.pop_back();
            dq.push_back(nums[i]);
        }
        int left = 0;
        vector<int> ans{dq.front()};
        for(int i = k; i < nums.size(); i++) {
            if(nums[left] == dq.front()) dq.pop_front();
            while(!dq.empty() && dq.back() < nums[i]) dq.pop_back();
            dq.push_back(nums[i]);
            ans.push_back(dq.front());
            left++;
        }
        return ans;

    }
};