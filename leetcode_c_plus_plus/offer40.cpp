// 剑指 Offer 40. 最小的k个数
// https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
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
@File : offer40.cpp
@Time : 2021/12/12 20:40:07
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        vector<int> ans;
        sort(arr.begin(), arr.end());
        for(int i = 0; i < k; i++) ans.push_back(arr[i]);
        return ans;
    }
};