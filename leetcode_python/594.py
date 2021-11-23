# 594. 最长和谐子序列
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 594.py
@Time : 2021/11/21 16:58:05
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
# 煞笔啊
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        d = sorted(d.items(), key = lambda key: key[0])
        ans = 0
        for i in range(1, len(d)):
            if d[i][0] - d[i - 1][0] == 1:
                ans = max(ans, d[i][1] + d[i - 1][1])
        return ans

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max((val + cnt[key + 1] for key, val in cnt.items() if key + 1 in cnt), default=0)
