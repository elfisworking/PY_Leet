// 剑指 Offer 42. 连续子数组的最大和
// https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
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
@File : offer42.cpp
@Time : 2021/12/05 21:28:27
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> prefix;
        prefix.push_back(0);
        for(auto x : nums) prefix.push_back(prefix.back() + x);
        int minVal = prefix[0];
        int ans = prefix[1];
        for(int i = 1; i < prefix.size(); i++) {
            ans = max(ans, prefix[i] - minVal);
            minVal = min(minVal, prefix[i]);
        }
        return ans;
    }
};