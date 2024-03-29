#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 48.py
@Time : 2021/07/12 11:04:43
@Author : YuMin Zhang
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0 , 0
        l = len(s) 
        h = set()
        res = 0
        while right < l:
            while s[right] in h:
                h.remove(s[left])
                left += 1
            h.add(s[right])
            res = max(res,right-left+1)
            right += 1
        return res
