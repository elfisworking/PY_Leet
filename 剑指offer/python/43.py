# 剑指 Offer 43. 1～n 整数中 1 出现的次数
# https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 43.py
@Time : 2021/07/09 14:37:44
@Author : YuMin Zhang
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        不会做 不会做  搜索的方式估计行不通
        '''
        digit , res = 1, 0 
        high , cur , low = n//10 , n%10 , 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high*digit
            elif cur == 1:
                res += high*digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res
s = Solution()
print(s.countDigitOne(1000))
