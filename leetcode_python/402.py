# 402. 移掉 K 位数字
# https://leetcode-cn.com/problems/remove-k-digits/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 402.py
@Time : 2022/03/16 22:20:30
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num)
        right_val = 0
        for i in range(k, l):
            right_val = right_val * 10 + int(num[i])
        length = l - k
        times = 10 ** (length - 1)
        left_val = 0
        min_val = right_val
        for i in range(l - k):
            left_val = left_val * 10 + int(num[i])
            right_val = right_val % times
            length -= 1
            times = times // 10
            min_val = min(min_val, left_val * (10 ** length) + right_val)
        return str(min_val)

s = Solution()
print(s.removeKdigits("10200", 1))