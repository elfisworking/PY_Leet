# 2032. 至少在两个数组中出现的值
# https://leetcode-cn.com/problems/two-out-of-three/
from typing import List
from collections import defaultdict
from collections import deque
from collections import Counter
from math import inf
import bisect
import heapq
'''
@File : 2032.py
@Time : 2022/03/15 16:50:34
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s = Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        return [i for i in s.keys() if s[i] > 1]
