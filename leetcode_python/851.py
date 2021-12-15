# 851. 喧闹和富有
# https://leetcode-cn.com/problems/loud-and-rich/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 851.py
@Time : 2021/12/15 13:21:08
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for r in richer:
            g[r[0]].append(r[1])
            inDeg[r[1]] += 1

        ans = list(range(n))
        q = deque(i for i, deg in enumerate(inDeg) if deg == 0)
        while q:
            x = q.popleft()
            for y in g[x]:
                if quiet[ans[x]] < quiet[ans[y]]:
                    ans[y] = ans[x]  # 更新 x 的邻居的答案
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return ans
