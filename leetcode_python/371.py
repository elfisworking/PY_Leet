# 371. 两整数之和
# https://leetcode-cn.com/problems/sum-of-two-integers/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 371.py
@Time : 2021/10/04 13:08:06
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : xor operation can do add operation , and opeation can do carray opeaation
'''
MASK1 = 4294967296 # 2^32
MASK2 = 2147483648 # 2^31
MASK3 = 2147483647  # 2^31-1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = ( a ^ b) % MASK1
            b = carry
        if a & MASK2: # negative
            return ~ ((a ^ MASK2) ^ MASK3)
        else: # positive 
            return a
s = Solution()
print(s.getSum(-12, -8))
