# 537. 复数乘法
# https://leetcode-cn.com/problems/complex-number-multiplication/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 537.py
@Time : 2022/02/25 23:37:04
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        real_num1 = int(num1[0])
        real_num2 = int(num2[0])
        vir_num1 = int(num1[1][:-1]) 
        vir_num2 = int(num2[1][:-1])
        real_num = real_num1 * real_num2 - vir_num1 * vir_num2
        vir_num = real_num1 * vir_num2 + real_num2 * vir_num1
        ans = str(real_num) + "+" + str(vir_num) + "i"
        return ans