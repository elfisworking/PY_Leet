# 1846. 减小和重新排列数组后的最大元素
# https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1846.py
@Time : 2021/07/26 09:48:39
@Author : YuMin Zhang
@Thinking : 想多了,本质贪心算法
'''
class Solution:
    # def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    #     # 时间复杂度为O(nlogn)
    #     arr.sort()
    #     arr[0] = 1
    #     l = len(arr)
    #     for i in range(1,l):
    #         if arr[i] - arr[i-1] > 1:
    #             arr[i] = arr[i-1] + 1

    #     return arr[l-1]
    
    # 时间复杂度为O(n)的算法 ????
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        l = len(arr)
        cnt = [0]*(l+1)
        # 计数
        for a in arr:
            cnt[min(a,l)] += 1
        limit = 0
        for i in range(1,l+1):
            limit = min(i,limit+cnt[i])
        return limit
s = Solution()
print(s.maximumElementAfterDecrementingAndRearranging([1,2,2,6,1]))