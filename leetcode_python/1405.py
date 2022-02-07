# 1405. 最长快乐字符串
# https://leetcode-cn.com/problems/longest-happy-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1405.py
@Time : 2022/02/07 22:46:04
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [[a, "a"], [b, "b"], [c, "c"]]
        ans = []
        while True:
            d.sort(key = lambda x : x[0], reverse = True)
            hasNext = True
            for i in range(3):
                if len(ans) >= 2 and ans[-2] == d[i][1] and ans[-1] == d[i][1]:
                    continue
                if d[i][0] > 0:
                    d[i][0] -= 1
                    ans.append(d[i][1])
                else:
                    hasNext = False
                break
            if not hasNext:
                return "".join(ans)
                break
        return ans
            
