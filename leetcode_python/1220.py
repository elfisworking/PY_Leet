# 1220. 统计元音字母序列的数目
# https://leetcode-cn.com/problems/count-vowels-permutation/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1220.py
@Time : 2022/01/17 10:02:16
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Hard
'''
# 超时
# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         ans = 0
#         letter = ["a","e","i","o","u"]
#         mod = 10 ** 9 + 7
#         def dfs(pre, length):
#             if length == n:
#                 nonlocal ans
#                 nonlocal mod
#                 ans = (ans + 1) % mod
#                 return 
#             for i in letter:
#                 if pre:
#                     if pre == "a" and i == "e":
#                         dfs(i, length + 1)
#                     elif pre == "e" and (i == "a" or i == "i"):
#                         dfs(i, length + 1)
#                     elif pre == "i" and i != "i":
#                         dfs(i, length + 1)
#                     elif pre == "o" and (i == "i" or i == "u"):
#                         dfs(i , length + 1)
#                     elif pre == "u" and i == "a":
#                         dfs(i, length + 1)
#                 else:
#                     dfs(i, length + 1)
#         dfs(None, 0)
#         return ans
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007
