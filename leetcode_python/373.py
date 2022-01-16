# 373. 查找和最小的 K 对数字
# https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 373.py
@Time : 2022/01/15 19:58:48
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        h = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        heapq.heapify(h)
        i = 0
        while i < k and h:
            _, a, b = heapq.heappop(h) 
            i += 1
            if b + 1 < len(nums2):
                heapq.heappush(h, (nums1[a], nums2[b], a, b + 1))
            ans.append((nums1[a], nums2[b]))
        return ans

s = Solution()
print(s.kSmallestPairs([1,2],[3], 3))