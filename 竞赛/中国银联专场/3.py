# 银联-03. 理财产品
# https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/I4mOGz/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 3.py
@Time : 2022/03/17 22:18:36
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxInvestment(self, product: List[int], limit: int) -> int:
        left = 0
        right = max(product)
        while left < right:
            mid = (left + right + 1) // 2
            S = sum( i - mid + 1 for i in product if i >= mid)
            if S >= limit:
                left = mid
            else:
                right = mid - 1
        print(left)
        ans = 0
        curr = 0
        for s in product:
            if s >= left:
                ans += (s - left + 1) * (s + left) // 2
                curr += s - left + 1
        ans -= (curr - limit) * left
        return ans % 1000000007
        