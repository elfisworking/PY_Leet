# 1713. 得到子序列的最少操作次数
# https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1713.py
@Time : 2021/07/26 11:06:40
@Author : YuMin Zhang
@State : Nonindepedent
@Thinking : 将其转化为求最长公共子序列，然后减一下就可以了。但是由于数据量的问题，无法使用dp的做法，需要使用二分和贪心的思想。
'''
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        pos = {}
        for i , t in enumerate(target):
            pos[t] = i
        
        d = []
        for val in arr:
            if val in pos:
                idx = pos[val]
                site = bisect.bisect_left(d,idx)
                if site  < len(d):
                    d[site] = idx
                else:
                    d.append(idx)
        
        return n - len(d)
                
