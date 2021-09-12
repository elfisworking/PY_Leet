# 剑指 Offer II 010. 和为 k 的子数组
# https://leetcode-cn.com/problems/QTMn0o/
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        pre = [0] * (l+1)
        for i in range(1,l+1):
            pre[i] = pre[i-1] + nums[i-1]

        h = defaultdict(int)
        h[0] = 1
        res = 0
        for i in range(1,l+1):
            sub = pre[i] - k 
            if sub in h:
                res += h[sub]
            h[pre[i]] += 1
        return res

