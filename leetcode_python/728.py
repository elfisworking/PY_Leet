# 728. 自除数
# https://leetcode-cn.com/problems/self-dividing-numbers/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 728.py
@Time : 2022/03/17 10:53:07
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num):
            tmp = num
            while tmp > 0:
                divisor = tmp % 10
                tmp = tmp // 10
                if divisor == 0 or num % divisor != 0:
                    return False
            return True
        ans = []
        for num in range(left, right + 1):
            if check(num):
                ans.append(num)
        return ans