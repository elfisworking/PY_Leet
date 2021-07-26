# 剑指offer 57-II 和为s的连续正数序列
# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 57-2.py
@Time : 2021/07/26 14:42:05
@Author : YuMin Zhang
@State : Half-independent
@Thinking : 数学方法，连续的话要考虑前缀和加哈希表的组合，滑动窗口等方法
'''
class Solution:
    # 数学方法
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        mid = target//2 + 2
        ans = []
        for n in range(2,mid):
            m = (n-1)*n/2
            if m >= target:
                break
            res = (target - m) % n
            if res == 0:
                x = (target - m) / n
                ans.append([int(x+i) for i in range(n)])
        ans = sorted(ans,key=lambda x:x[0])
        return ans
s = Solution()
print(s.findContinuousSequence(9))
