# 412. Fizz Buzz
# https://leetcode-cn.com/problems/fizz-buzz/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 412.py
@Time : 2021/10/13 21:31:00
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            a = i%3
            b = i%5
            if not a and not b:
                ans.append("FizzBuzz")
            elif not a:
                ans.append("Fizz")
            elif not b:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
