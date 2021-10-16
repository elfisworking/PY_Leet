# 282. 给表达式添加运算符
# https://leetcode-cn.com/problems/expression-add-operators/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 282.py
@Time : 2021/10/16 10:09:43
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr, i, res, mul):
            if i == n:
                if res == target:
                    ans.append("".join(expr))
                return 
            signIndex = len(expr)
            if  i > 0:
                expr.append("")
            val = 0
            for j in range(i, n):
                if j > i  and num[i] == "0":
                    break
                val = 10 * val + int(num[j])
                expr.append(num[j])
                if i == 0:
                    backtrack(expr, j + 1, val, val)
                else:
                    # 枚举符号
                    expr[signIndex] = "+"; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = "-"; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = "*"; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]
        
        backtrack([], 0, 0, 0)
        return ans
                    
