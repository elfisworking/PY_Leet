# 2191. 将杂乱无章的数字排序
# https://leetcode-cn.com/problems/sort-the-jumbled-numbers/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 2191.py
@Time : 2022/04/28 23:29:15
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transfer(x: int) -> int:
            return int("".join(str(mapping[int(digit)]) for digit in str(x)))
        
        num_pairs = [(transfer(num), num) for num in nums]
        num_pairs.sort(key=lambda pair: pair[0])
        
        ans = [num for (_, num) in num_pairs]
        return ans