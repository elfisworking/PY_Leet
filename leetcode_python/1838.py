# 1838. 最高频元素的频数
# https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1838.py
@Time : 2021/07/25 21:07:16
@Author : YuMin Zhang
@Thinking : 
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
