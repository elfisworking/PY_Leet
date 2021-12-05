// 剑指 Offer 63. 股票的最大利润
// https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
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
@File : offer63.cpp
@Time : 2021/12/05 21:15:06
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) return 0;
        int ans = 0;
        int minVal = prices[0];
        for(int i = 0; i < prices.size(); i++) {
            minVal = min(minVal, prices[i]);
            ans = max(ans, prices[i] - minVal); 
        }

        return ans;
    }
};