#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1185.py
@Time : 2022/01/03 20:12:00
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days = 0
        # 输入年份之前的年份的天数贡献
        days += 365 * (year - 1971) + (year - 1969) // 4
        print(days)
        # 输入年份中，输入月份之前的月份的天数贡献
        days += sum(monthDays[:month-1])
        print(days)
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month >= 3:
            days += 1
        # 输入月份中的天数贡献
        days += day
        print(days)
        return week[(days + 3) % 7]
"""
我理解的是1971-2100年之间都是四年一闰，
没有400的倍数。1972年是闰年，但是该题算法是计算当年之前的天数，再加上当年的天数，再加上当年是否是闰年的一天，
所以到1973年才能加上贡献的天数，所以是1973-4=1969。
"""
s = Solution()
print(s.dayOfTheWeek(15, 7 ,1987))