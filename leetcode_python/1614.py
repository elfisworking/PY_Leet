# 1614. 括号的最大嵌套深度
# https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1614.py
@Time : 2022/01/07 19:50:23
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == "(":
                stack.append("(")
                ans = max(ans, len(stack))
            elif i == ")":
                stack.pop()
        return ans 