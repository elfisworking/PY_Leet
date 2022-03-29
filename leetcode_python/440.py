# 440. 字典序的第K小数字
# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 440.py
@Time : 2022/03/24 22:42:57
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def getSteps(self, cur: int, n: int) -> int:
        steps, first, last = 0, cur, cur
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            steps = self.getSteps(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur

class Solution:
    def getSteps(self, curr, n):
        steps, left, right = 0, curr, curr
        while left <= n:
            steps += min(n, right) - left + 1
            left = 10 * left
            right = 10 * right + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k:
            nums = self.getSteps(curr, n)
            print(nums)
            if nums <= k:
                k -= nums
                curr += 1
            else:
                k -= 1
                curr = curr * 10
        return curr