#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1995.py
@Time : 2021/12/29 10:46:46
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        s = defaultdict(int)
        ans = 0
        def dfs(index, n, depth):
            if depth < 3:
                for i in range(index , len(nums)):
                    dfs(i + 1, n + nums[i], depth + 1)
            else:
                nonlocal ans
                for i in range(index, len(nums)):
                    if nums[i] == n:
                        ans += 1
        dfs(0, 0, 0)
        return ans
                    


s = Solution()
print(s.countQuadruplets([9,6,8,23,39,23]))
