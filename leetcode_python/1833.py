# 1833. 雪糕的最大数量
# https://leetcode-cn.com/problems/maximum-ice-cream-bars/

# 贪心算法
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for i in costs:
            if i <= coins:
                ans += 1 
                coins -= i
            else:
                break
        return ans