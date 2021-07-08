# 442. 数组中重复的数据
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 442.py
@Time : 2021/07/08 17:45:16
@Author : YuMin Zhang
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        微软面试题  
        思路: 利用数组下标 
        比起 +length 取相反数会更有效
        '''
        ans = []
        l = len(nums)
        i = 0 
        while i < l:
            val = nums[i]
            if l<  val <= 2*l :
                val -= l
            elif val > 2*l:
                val -= 2 *l
            nums[val-1] += l
            i += 1
        
        for i  in range(l):
            if nums[i] > 2*l:
                ans.append(i+1)
        
        return ans