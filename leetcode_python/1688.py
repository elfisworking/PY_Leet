# 1688. 比赛中的配对次数
# https://leetcode-cn.com/problems/count-of-matches-in-tournament/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1688.py
@Time : 2022/01/25 16:34:41
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                ans += n
            else:
                n = (n - 1) // 2
                ans += n
                n += 1
        return ans

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1