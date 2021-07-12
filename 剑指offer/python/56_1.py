# 剑指 Offer 56 - I. 数组中数字出现的次数
# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
import functools
'''
@File : 56_1.py
@Time : 2021/07/12 09:56:38
@Author : YuMin Zhang
'''
class Solution:
    def singleNumbers(self,nums:List[int]) -> List[int]:
        # 异或运算 第一次的异或运算找到两个只出现一次的数它们不同的位
        # 然后根据这个不同的位 进行分组异或
        ret = functools.reduce(lambda x, y : x ^ y,nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a , b = 0 , 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
