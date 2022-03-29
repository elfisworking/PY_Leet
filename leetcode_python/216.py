# 216. 组合总和 III
# https://leetcode-cn.com/problems/combination-sum-iii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 216.py
@Time : 2022/03/24 22:16:38
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        use = [0 for _ in range(10)]
        ans = []
        def dfs(currSum, depth, conbine, start):
            if depth == k:
                if currSum == n:
                    ans.append(conbine[:])
                return 
            for i in range(start, 10):
                if use[i] == 1:
                    continue
                use[i] = 1
                conbine.append(i)
                dfs(currSum + i, depth + 1, conbine, i)
                conbine.pop()
                use[i] = 0
        dfs(0, 0, [], 1)
        return ans