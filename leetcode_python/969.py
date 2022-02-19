# 969. 煎饼排序
# https://leetcode-cn.com/problems/pancake-sorting/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 969.py
@Time : 2022/02/19 23:31:04
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        arr_copy = arr[:]
        arr_copy.sort()
        l = len(arr_copy)
        ptr = l - 1
        ans = []
        def reverse(k):
            left, right = 0, k -1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        while ptr > 0:
            val = arr_copy[ptr]
            idx = arr.index(val)
            if idx != ptr:
                if idx != 0:
                    ans.append(idx + 1)
                    reverse(idx + 1)
                ans.append(ptr + 1)
                reverse(ptr + 1)
            ptr -= 1
        return ans