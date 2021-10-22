# 66. 加一
# https://leetcode-cn.com/problems/plus-one/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 66.py
@Time : 2021/10/21 22:34:25
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     num = 0
    #     for i in digits:
    #         num = num * 10 + i
    #     num += 1
    #     ans = []
    #     while num != 0:
    #         mod = num % 10
    #         ans.append(mod)
    #         num = num // 10
    #     return ans[::-1]
    # 模拟进位
    def plusOne(self, digits: List[int]) -> List[int]: 
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0 :
                return digits
        digits = [1] + digits
        return digits