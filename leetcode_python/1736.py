# https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/
# 1736. 替换隐藏数字得到的最晚时间
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1736.py
@Time : 2021/07/25 13:45:24
@Author : YuMin Zhang
'''
class Solution:
    def maximumTime(self, time: str) -> str:
        ans = []
        l = len(time)
        for i in range(l):
            if time[i] == "?":
                if i == 0:
                    if time[1] == "?" or int(time[1]) < 4:
                        ans.append("2")
                    else:
                        ans.append("1")
                else:
                    if i == 1 and ans[-1] == "2":
                        ans.append("3")
                    elif ans[-1] == ":":
                        ans.append("5")
                    else:
                        ans.append("9")
            else:
                ans.append(time[i])

            
        return "".join(ans)


