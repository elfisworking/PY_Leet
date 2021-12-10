# 689. 三个无重叠子数组的最大和
# https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 689.py
@Time : 2021/12/08 21:48:32
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        sum2, maxSum12, maxSum12Idx = 0, 0, ()
        sum3, maxTotal = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i - k * 3 + 1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = [0]
        for i in nums: 
            s.append(s[-1] + i)
        
        f = [[0]* 4 for _ in range(n + 2)]
        for i in range(n - k + 1, 0, -1):
            for j in range(1,4):
                f[i][j] = max(f[i + 1][j], f[i + k][j - 1] + s[i + k - 1] - s[i - 1])
        
        ans = [0] * 3
        i , j , idx = 1 , 3, 0
        while j > 0 :
            if f[i + 1][j] > f[i + k][j - 1] + s[i + k - 1] - s[i - 1]:
                i += 1
            else:
                ans[idx] = i - 1
                idx += 1
                i += k
                j -= 1
        return ans
s  = Solution()
print(s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))