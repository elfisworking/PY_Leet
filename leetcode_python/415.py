# 415. 字符串相加
# https://leetcode-cn.com/problems/add-strings/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 415.py
@Time : 2022/03/16 22:02:04
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ans = ""
        l1 = len(num1)
        l2 = len(num2)
        ptr1  = l1 - 1
        ptr2 = l2 - 1
        while ptr1 >= 0 or ptr2 >=0 or carry > 0:
            a = int(num1[ptr1]) if ptr1 >= 0 else 0
            b = int(num2[ptr2]) if ptr2 >= 0 else 0
            c = a + b + carry
            ans = str(c % 10) + ans
            carry = c //  10
            ptr1 -= 1
            ptr2 -= 1
        return ans