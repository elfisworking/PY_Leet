// 剑指 Offer 45. 把数组排成最小的数
// https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
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
@File : offer45.cpp
@Time : 2021/12/12 20:19:19
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    string minNumber(vector<int>& nums) {
        vector<string> strs;
        string ans;
        for(auto x : nums) strs.push_back(to_string(x));
        // reference is important
        sort(strs.begin(), strs.end(), [](string &s1, string & s2) {return s1 + s2 < s2 + s1;});
        for(auto x : strs) ans += x;
        return ans;
    }
};