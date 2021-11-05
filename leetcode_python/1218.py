# 1218. 最长定差子序列
# https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1218.py
@Time : 2021/11/05 22:46:05
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : dp
'''
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        l = len(arr)
        d = {arr[0]:1}
        dp = [1] * l
        for i in range(1, l):
            num = arr[i] - difference
            if num in d:
                dp[i] += d[num]           
                if arr[i] not in d:
                    d[arr[i]] = dp[i]
                else:
                    d[arr[i]] = max(d[arr[i]], dp[i])
            else:
                d[arr[i]] = dp[i]
        ans = max(dp)
        return ans

    # 对于两个相同的元素，下标较大的元素对应的dp 值不会小于下标较小的元素对应dp 值
    # 一开始写没有想到，可以用反证法证明
    def longestSubsequence_offical(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int) # 用defualtint 这个很巧妙
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())

