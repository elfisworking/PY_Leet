# 2024. 考试的最大困扰度
# https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2024.py
@Time : 2022/03/11 23:18:36
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        m = defaultdict(int)
        n, l, ans = len(a), 0, 0
        for r in range(n):
            m[a[r]] += 1
            if min(m["T"], m["F"]) > k:
                m[a[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans