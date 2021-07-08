# 930. 和相同的二元子数组
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 930.py
@Time : 2021/07/08 11:34:02
@Author : YuMin Zhang
'''
class Solution:
    def numSubarraysWithSum_hash_and_prefix(self, nums: List[int], goal: int) -> int:
        '''
        哈希表 + 前缀和
        要注意到 nums 具有非严格单调递增的特性
        '''
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for i in range(1,len(prefix)):
            diff = prefix[i] -goal
            ans += d[diff]
            d[prefix[i]] += 1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = len(nums)
        ans = l1 = l2 = s1 = s2 = 0
        for r in range(l):
            s1 += nums[r]
            s2 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ans += l2 - l1
        return ans
s = Solution()
print(s.numSubarraysWithSum([1,0,1,0,1],2))