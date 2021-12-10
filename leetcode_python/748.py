# 748. 最短补全词
# https://leetcode-cn.com/problems/shortest-completing-word/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 748.py
@Time : 2021/12/10 14:04:33
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        d = defaultdict(int)
        for i in licensePlate:
            if ord('a') <= ord(i) <= ord("z"):
                d[i] += 1
        ans = None
        for i in words:
            c = Counter(i)
            flag = True
            for k, v in d.items():
                if c[k] < v:
                    flag = False
                    break
            if flag:
                if ans == None or len(ans) > len(i):
                    ans = i
        return ans
            