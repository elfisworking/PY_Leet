# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# 714. 买卖股票的最佳时机含手续费
from curses.ascii import SO
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 714.py
@Time : 2022/03/17 11:03:46
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        dp = [[0] * l for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, l):
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i])
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i] - fee)
        return dp[0][l - 1]
s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))