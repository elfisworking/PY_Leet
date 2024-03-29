#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 45.py
@Time : 2021/07/11 10:03:53
@Author : YuMin Zhang
'''
class Solution:
    def minNumber(self,nums:List[int]) -> str:
        def quick_sort(l,r):
            if l>=r: return 
            i , j = l , r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] , strs[j],strs[i]
            strs[i], strs[l] = strs[l],strs[i]
            quick_sort(l,i-1)
            quick_sort(i+1,r)


        strs = [str(num) for num in nums]
        quick_sort(0,len(strs)-1)
        return "".join(strs)