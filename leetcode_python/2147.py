# 2147. 分隔长廊的方案数
# https://leetcode-cn.com/problems/number-of-ways-to-divide-a-long-corridor/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2147.py
@Time : 2022/01/27 14:47:17
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Hard
'''
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        counter = Counter(corridor)
        if counter["S"] == 0 or counter["S"] % 2 == 1:
            return 0
        right = 0
        counter = 0
        ans = 1
        mod = 10**9 + 7
        while right < len(corridor):
            if corridor[right] == "S":
                counter += 1
            if counter == 2:
                right += 1
                tmp = 0
                while right < len(corridor) and corridor[right] != "S":
                    tmp += 1
                    right += 1
                if right < len(corridor) and corridor[right] == "S":
                    ans = (ans * (tmp + 1)) % mod
                counter = 0
            else:
                right += 1
        return ans