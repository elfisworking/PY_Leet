// 121. 买卖股票的最佳时机
//  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
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
@File : 121.cpp
@Time : 2022/01/02 19:45:47
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
**/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int min_val = prices[0];
        for(int i = 1; i < prices.size(); i++) {
            if(min_val > prices[i]) {
                min_val = prices[i];
            } else {
                ans = max(ans, prices[i] - min_val);
            }
        }
        return ans;


    }
};