# 2011. 执行操作后的变量值
# https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2011.py
@Time : 2022/03/15 16:31:19
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in operations:
            if "--" in i:
                ans -= 1
            else:
                ans += 1
        return ans
