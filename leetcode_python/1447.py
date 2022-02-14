# 1447. 最简分数
# https://leetcode-cn.com/problems/simplified-fractions/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1447.py
@Time : 2022/02/10 22:27:19
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        def check(i, j):
            for a in range(2, min(i, j) + 1):
                if i % a == 0 and j % a == 0:
                    return False
            return True

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if check(i, j):
                    ans.append(str(i) + "/" + str(j))
        return ans