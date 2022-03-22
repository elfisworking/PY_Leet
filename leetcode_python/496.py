# 496. 下一个更大元素 I
# https://leetcode-cn.com/problems/next-greater-element-i/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 496.py
@Time : 2022/03/18 20:47:23
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                d[nums2[i]] = stack[-1]
            else:
                d[nums2[i]] = -1
            stack.append(nums2[i])
        ans = []
        for i in nums1:
            ans.append(d[i])
        return ans