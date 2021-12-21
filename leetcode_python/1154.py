# 1154. 一年中的第几天
# https://leetcode-cn.com/problems/day-of-the-year/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1154.py
@Time : 2021/12/21 10:09:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking : 考察闰年的计算方式，能被4整除但是不能被100整除 或者 能够被400整除的 年份
@Tag : Easy
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(x) for x in date.split("-")]

        amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            amount[1] += 1

        ans = sum(amount[:month - 1])
        return ans + day
