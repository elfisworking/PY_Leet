# 128. 最长连续序列
# https://leetcode-cn.com/problems/longest-consecutive-sequence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 128.py
@Time : 2022/02/20 22:42:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        ans = 0
        for num in num_s:
            if num - 1 not in num_s:
                cur_num = num
                cur_step = 1
                while cur_num + 1 in num_s:
                    cur_num += 1
                    cur_step += 1
                ans = max(ans, cur_step)
        return ans