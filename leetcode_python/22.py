# 22. 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 22.py
@Time : 2022/01/16 14:04:35
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = n
        right = n
        ans = []
        def recursion(path:list, left, right):
            if left == 0 and right == 0:
                ans.append("".join(path))
                return
            if left > 0: 
                path.append("(")
                recursion(path, left - 1, right)
                path.pop()
            if left < right:
                path.append(")")
                recursion(path, left, right - 1)
                path.pop()
            

        recursion([], left, right)
        return ans