# 2044. 统计按位或能得到最大值的子集数目
# https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2044.py
@Time : 2022/03/15 16:23:34
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if not nums:
            return nums
        max_value = nums[0]
        l = len(nums)
        for i in range(1, len(nums)):
            max_value |= nums[i]
        print(max_value)
        bits = (1 << l) - 1
        ans = 0
        while bits > 0:
            tmp = None
            print(1, bits)
            for i in range(l):
                bit = bits & (1 << i)
                if bit > 0:
                    if tmp == None:
                        tmp = nums[i]
                    else:
                        tmp |= nums[i]
            if tmp == max_value:
                print(2, bits)
                ans += 1
            bits -= 1
        return ans

s = Solution()
print(s.countMaxOrSubsets([3,2,1,5]))