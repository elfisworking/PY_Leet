# 400. 第 N 位数字
# https://leetcode-cn.com/problems/nth-digit/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 400.py
@Time : 2021/11/30 10:11:36
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        end = 9
        k = 1
        while n > (end * k):
            n -= end * k
            k += 1
            end = end * 10
        begin = end // 9
        a = (n - 1) // k
        num = str(begin + a)
        b = (n - 1) % k
        return int(num[b])

if __name__ == "__main__":
    s = Solution()
    s.findNthDigit(13)