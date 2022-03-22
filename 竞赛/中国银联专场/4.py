# 银联-04. 合作开发
# https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/lCh58I/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 4.py
@Time : 2022/03/17 22:19:22
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def coopDevelop(self, skills: List[List[int]]) -> int:
        def my_hash(s):
            res = 0
            for x in s:
                res <<= 10
                res += x 
            return res
        c = Counter()
        n = len(skills)
        for i in range(n):
            skills[i].sort()
        for i in range(n):
            c[my_hash(skills[i])] += 1
        cnt = 0
        for key in c:
            cnt += c[key] * (c[key] - 1) // 2
        for i in range(n):
              for j in range(1, len(skills[i])):
                    for a in itertools.combinations(skills[i], j):
                        cnt += c[my_hash(a)]
        p = 10 ** 9 + 7
        return (n * (n - 1) // 2 - cnt) % p