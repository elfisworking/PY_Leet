// 122. 买卖股票的最佳时机 II
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
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
@File : 122.cpp
@Time : 2022/01/19 22:45:02
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() <= 0) return 0;
        int left = 0;
        int right = 0;
        int ans = 0;
        while(right < prices.size()) {
            if(right > 0 && prices[right] < prices[right - 1]) {
                ans += prices[right - 1] - prices[left];
                left = right;
            }
            right++;
        }
        ans += prices[right - 1] - prices[left];
        return ans;

    }
};
// dp思想 转换思路 将正负考虑进去
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp0 = 0, dp1 = -prices[0];
        for (int i = 1; i < n; ++i) {
            int newDp0 = max(dp0, dp1 + prices[i]);
            int newDp1 = max(dp1, dp0 - prices[i]);
            dp0 = newDp0;
            dp1 = newDp1;
        }
        return dp0;
    }
};