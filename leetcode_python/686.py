# 686. 重复叠加字符串匹配
# https://leetcode-cn.com/problems/repeated-string-match/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 686.py
@Time : 2021/12/22 10:15:48
@Author : YuMin Zhang
@State : Indepeedent | Depedent 
@Thinking :
@Tag : Medium
'''

# 没有考虑 a: “aaac”  b: "aac" 这种情况
# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         if not b: return 0
#         j = 0 
#         l = len(a)
#         for i in range(l):
#             if a[i] == b[0]:
#                 j = i
#                 break
#         if j == 0 and a[j] != b[0]:
#             return -1
#         print(j)
#         j += 1
#         ans = 1
#         for i in range(1, len(b)):
#             j = j % l
#             if a[j] == b[i]:
#                 if j == 0:
#                     ans += 1
#                 j += 1
#             else:
#                 return -1


#         return ans

# 错误
# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         if not b: return 0
#         j = 0 
#         l = len(a)
#         for i in range(l):
#             if l -i <= len(b) and a[i:l] == b[:l - i]:
#                 j = l - i
#                 break
#         print(j)
#         if j == 0 :
#             return -1
#         print(j)
#         ans = 1
#         m = 0
#         for i in range(j, len(b)):
#             m = m % l
#             if a[m] == b[i]:
#                 if m == 0:
#                     ans += 1
#                 m += 1
#             else:
#                 return -1


#         return ans

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        l1, l2 = len(a), len(b)
        s = ""
        ans = 0
        while len(s) < l2:
            s += a
            ans += 1
        s += a
        idx = s.find(b)
        if idx == -1: return -1
        return ans + 1 if idx + l2 > l1 * ans else ans


# 关于 find 方法 需要看以下 KMP算法 和 RJ算法