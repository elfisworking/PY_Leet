# 38. 外观数列
# https://leetcode-cn.com/problems/count-and-say/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 38.py
@Time : 2021/10/15 21:31:07
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        strs = self.countAndSay(n - 1)
        ans = []
        count = 0
        char = None
        for ch in strs:
            if not char:
                char = ch
            if char == ch:
                count += 1
            else:
                ans.append(str(count))
                ans.append(char)
                char = ch
                count = 1
        ans.append(str(count))
        ans.append(char)
        return "".join(ans)