#
#
from curses.ascii import SO
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 564.py
@Time : 2022/03/02 17:25:59
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
## ERROR
# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#         l = len(n)
#         if l == 1:
#             return str(int(n) - 1)
#         change = False
#         left , right = 0, l - 1
#         ans = list(n)
#         while left <right:
#             if ans[right] == ans[left]:
#                 right -= 1
#                 left += 1
#                 continue
#             ans[right] = ans[left]
#             left += 1
#             right -= 1
#             change = True
#         if not change:
#             odd = l // 2
#             if l % 2 == 1:
#                 num = int(ans[odd])
#                 if num == 0:
#                     left , right = odd - 1, odd
#                     while ans[left] == "0" or ans[right] == "0":
#                         if ans[left] == "0":
#                             ans[left] = "9"
#                             left -= 1
#                         if ans[right] == "0":
#                             ans[right] = "9"
#                             right += 1
#                     if left == 0 and ans[left] == "1":
#                         ans.pop()
#                         ans.pop(0)
#                         ans.apend("9")
#                     else:
#                         ans[left] = str(int(ans[left]) - 1)
#                         ans[right] = str(int(ans[right]) - 1)
#                 else:
#                     ans[odd] = str(num - 1)
#             else:
#                 num = int(ans[odd])
#                 if num == 0:
#                     left , right = odd - 1, odd
#                     while ans[left] == "0" or ans[right] == "0":
#                         if ans[left] == "0":
#                             ans[left] = "9"
#                             left -= 1
#                         if ans[right] == "0":
#                             ans[right] = "9"
#                             right += 1
#                     if left == 0 and ans[left] == "1":
#                         ans.pop()
#                         ans.pop(0)
#                         ans.apend("9")
#                     else:
#                         ans[left] = str(int(ans[left]) - 1)
#                         ans[right] = str(int(ans[right]) - 1)
#                 else:
#                     ans[odd] = str(num - 1)
#                     ans[odd - 1] = str(num - 1)
#         return "".join(ans)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) -1, 10 ** m + 1]
        selfPrefix = int(n[:(m + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)
        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)
s = Solution()
print(s.nearestPalindromic("2100012"))