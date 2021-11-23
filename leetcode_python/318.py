#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
from functools import reduce
from itertools import product
import bisect
import heapq
'''
@File : 318.py
@Time : 2021/11/17 21:58:46
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 没有想到用位运算
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda a,b : a | (1 << (ord(b) - ord('a'))), word, 0)
                for word in words]
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), 
                repeat=2) if x[0] & y[0] == 0), default=0)
