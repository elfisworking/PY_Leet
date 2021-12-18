// 剑指 Offer 66. 构建乘积数组
// https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
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
@File : offer66.cpp
@Time : 2021/12/18 14:13:55
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        vector<int> prefix{1};
        for(int x : a) prefix.push_back(prefix.back() * x);
        int l = a.size();
        vector<int> prefix1{1};
        for(int i = l - 1; i >=0; i--) prefix1.push_back(prefix1.back() * a[i]);
        vector<int> ans;
        for(int i = 0; i < l ; i++) {
            ans.push_back(prefix[i] * prefix1[l - i - 1]);
        }
        return ans;
        
    }
};
