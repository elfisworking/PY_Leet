#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 375.py
@Time : 2021/11/12 21:32:36
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
# 第一次尝试 错误  后发现可能是动态规划题
# class Solution:
#     def getMoneyAmount(self, n: int) -> int:
#         prefix = [0]
#         for i in range(1, n + 1):
#             prefix.append(prefix[-1] + i)
#         def recursive(left, right):
#             if left == right:
#                 return 0
#             if right - left == 1:
#                 return left  
#             if right - left == 2:
#                 return left + 1
#             mid = left + 1
#             minus = prefix[right] - prefix[mid] - (prefix[mid - 1] - prefix[left - 1])
#             for i in range(left + 2, right):
#                 tmp = abs(prefix[right] - prefix[i] - prefix[i - 1] + prefix[left - 1])
#                 if tmp < minus:
#                     minus = tmp
#                     mid = i
#             l = recursive(left, mid - 1)
#             r = recursive(mid + 1, right)
#             print(mid, l, r)
#             return mid + max(l, r)
#         ans = recursive(1, n)
#         return ans 

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = min(k + max(f[i][k - 1], f[k + 1][j]) for k in range(i, j))
        return f[1][n]
