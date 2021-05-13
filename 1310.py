# 1310. 子数组异或查询
# https://leetcode-cn.com/problems/xor-queries-of-a-subarray/
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l = len(arr)
        dp = [0]
        for i in range(l):
            dp.append(dp[-1] ^ arr[i])
        res = []
        for left ,right  in queries:
            res.append(dp[left] ^ dp[right+1])
        return res