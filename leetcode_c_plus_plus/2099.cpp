// 2099. 找到和最大的长度为 K 的子序列
// https://leetcode-cn.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
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
@File : 2099.cpp
@Time : 2022/04/03 15:56:37
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<pair<int, int>> n;
        for(int i = 0; i < nums.size(); i++){
            n.push_back(pair<int, int>(i, nums[i]));
        }
        sort(n.begin(), n.end(), [&](pair<int, int> a, pair<int, int>b){ return a.second> b.second;});
        sort(n.begin(), n.begin() + k);
        vector<int> ans;
        for(int i = 0; i < k; i++) {
            ans.push_back(n[i].second);
        }
        return ans;
        
    }
};