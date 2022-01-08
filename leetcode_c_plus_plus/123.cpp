//
//
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
@File : 123.cpp
@Time : 2022/01/08 19:48:57
@Author : YuMin Zhang
@State :Depedent 
@Thinking :
@Tag : Hard
**/
class Solution {
public:
         int maxProfit(vector<int>& prices) {

         int n = prices.size();
         int buy1 = prices[0], sell1 = 0;
         int buy2 = prices[0], sell2 = 0;
         for (int i = 1; i < n; ++i) {
             buy1 = min(buy1, prices[i]);
             sell1 = max(sell1, prices[i] - buy1);
             buy2 = min(buy2, prices[i] - sell1); // this is important
             sell2 = max(sell2, prices[i] - buy2);
         }
         return sell2;
     }
};