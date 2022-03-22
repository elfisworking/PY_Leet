# 1475. 商品折扣后的最终价格
# https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1475.py
@Time : 2022/03/19 20:59:03
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if not prices:
            return []
        l = len(prices)
        stack = []
        ans = [0] * l
        for i in range(l - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            ans[i] += prices[i]
            ans[i] -= stack[-1] if stack else 0
            stack.append(prices[i])
        return ans