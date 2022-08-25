# 6063. 节点序列的最大得分
# https://leetcode-cn.com/problems/maximum-score-of-a-node-sequence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
import itertools
from heapq import nlargest

'''
@File : 6063.py
@Time : 2022/04/18 20:20:58
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for x, y in edges:
            g[x].append((scores[y], y))
            g[y].append((scores[x], x))
        for i, vs in enumerate(g):
            g[i] = nlargest(3, vs)
        ans = -1
        for x, y in edges:
            for (score_a, a), (score_b, b) in itertools.product(g[x], g[y]):
                if y != a != b != x:
                    ans = max(ans, score_a + scores[x] + scores[y] + score_b)
        return ans

s = Solution()
print(s.maximumScore([5,2,9,8,4], [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))


class Solution:
    def deleteText(self, a: str, index: int) -> str:\
        if a[index] == " ":
            return a
        else:
            left = index - 1
            right = index + 1
            while left >= 0 and a[left].isalpha():
                left -= 1
            while right < len(a) and a[right].isalpha():
                right += 1
            ans = [0:left] + [right:]
            return ans