# 剑指 Offer 56 - II. 数组中数字出现的次数 II
# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 56.py
@Time : 2021/07/26 13:25:58
@Author : YuMin Zhang
@State :  Half-Independent
@Thinking : 最简单的方法就是使用Map,进行查找，但是这种方法比较low。
'''
class Solution:
    # 使用哈希的方法
    # def singleNumber(self, nums: List[int]) -> int:
    #     d = defaultdict(int)
    #     for i in nums:
    #         d[i] += 1
    #     for k,v in d.items():
    #         if v == 1:
    #             return k
    #     return None
    
    # bit operation after mod 3 get number which appears once
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
