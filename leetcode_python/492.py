# 492. 构造矩形
# https://leetcode-cn.com/problems/construct-the-rectangle/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
from math import sqrt
'''
@File : 492.py
@Time : 2021/10/23 21:21:22
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]
