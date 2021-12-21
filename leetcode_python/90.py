# 90. 子集 II
# https://leetcode-cn.com/problems/subsets-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 90.py
@Time : 2021/12/21 19:49:21
@Author : YuMin Zhang
@State : Indepeedent
@Thinking : 关键处理重复子集
@Tag : Medium
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = [[]]
        l = len(nums)
        def dfs(path,index):
            for i in range(index, len(nums)):
                if i > index and nums[i] != nums[i - 1]:
                    path.append(nums[i])
                    ans.append(path[:])
                    dfs(path, i + 1)
                    path.pop()
                elif i == index:
                    path.append(nums[i])
                    ans.append(path[:])
                    dfs(path, i + 1)
                    path.pop()

        dfs([],0)
        return ans