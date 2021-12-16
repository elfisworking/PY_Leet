# 71. 简化路径
# https://leetcode-cn.com/problems/simplify-path/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 71.py
@Time : 2021/12/16 21:21:52
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        print(path)
        for i in path:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)
        ans = "/" + "/".join(stack)
        return ans