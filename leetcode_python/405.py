# 405. 数字转换为十六进制数
# https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 405.py
@Time : 2021/10/04 14:51:37
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
MASK = 4294967296
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        s = []
        def to_hex(a):
            if a < 10:
                return str(a)
            elif a == 10:
                return "a"
            elif a == 11:
                return "b"
            elif a == 12:
                return "c"
            elif a == 13:
                return "d"
            elif a == 14:
                return "e"
            elif a == 15:
                return "f"
        if num < 0:
            num = MASK + num
        while num > 0:
            a = num % 16
            a = to_hex(a)
            s.append(a)
            num = num // 16
        s.reverse()
        print(s)
        return "".join(s)
