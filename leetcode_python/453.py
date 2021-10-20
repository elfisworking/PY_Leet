# 453. 最小操作次数使数组元素相等
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 453.py
@Time : 2021/10/20 22:39:02
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
# class Solution:
#     超时
#     def minMoves(self, nums: List[int]) -> int:
#         def check(nums):
#             for i in range(1, len(nums)):
#                 if nums[i - 1] != nums[i]:
#                     return False
#             return True
#         ans = 0
#         count = 2**31
#         while ans < count:
#             if check(nums):
#                 return ans
#             else:
#                 max_value = max(nums)
#                 flag = True
#                 new_nums = []
#                 max_value = max(nums)
#                 for i in nums:
#                     if flag and i == max_value:
#                         flag = False
#                         new_nums.append(i)
#                         continue
#                     new_nums.append(i + 1)

#                 nums = new_nums
#                 print(nums)
#                 ans += 1
#                 return ans


class Solution:
    # 逆向思维
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        ans = 0
        for i in nums:
            ans += i - min_value
        return ans

# 公式思考的不全面
# class Solution:
#     def minMoves(self, nums: List[int]) -> int:
#         l = len(nums)
#         flag = True
#         for i in range(1, l):
#             if nums[ i - 1] != nums[i]:
#                 flag = False
#                 break
#         if flag:
#             return 0
#         max_value = max(nums)

#         mul = l - 1
#         while True:
#             val = 0
#             for i in nums:
#                 val += max_value - i
#             if val % mul == 0:
#                 return val // mul
#             max_value += 1


## 公式：
## ans = [(min_value + ans) * n - sum(nums) ] // n - 1
## 单纯的考虑 不是最终解
# for example
# [-100,0,100]
            

