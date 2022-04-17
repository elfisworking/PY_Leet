# 357. 统计各位数字都不同的数字个数
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 357.py
@Time : 2022/04/11 23:01:19
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        k = 0
        ans = 0
        prev = 81
        while k <= n:
            if k == 0:
                ans += 1
            elif k == 1:
                ans += 9
            elif k == 2:
                ans += 81
            else:
                prev = prev * (10 - k + 1)
                ans += prev
            k += 1
        return ans

s = Solution()
print(s)