# 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
# https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/
from typing import List
class Solution:
    # 前缀和  区间判断 贪心确定区间
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        l = len(queries)
        ans = []
        prefix = [0]
        for i in candiesCount:
            prefix.append(prefix[-1]+i)
        for q in queries:
            day = q[1]
            cap = q[2]
            count = (day+1) * cap
            if (day+1)<=prefix[q[0]+1]  and not(prefix[q[0]] >= count):
                ans.append(True)
            else:
                ans.append(False)
        return ans

