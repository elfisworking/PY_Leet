# 剑指 Offer 63. 股票的最大利润
# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        heap = [prices[0]]
        res = 0
        for i in range(1,len(prices)):
            if heap[0] < prices[i]:
                res = max(res,prices[i]-heap[0])
            heapq.heappush(heap,prices[i])
        return res