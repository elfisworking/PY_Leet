#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1818.py
@Time : 2021/07/14 14:42:15
@Author : YuMin Zhang
'''
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        l = len(nums1)
        nums1_clone = nums1.copy()
        nums1_clone.sort()
        sum, max_value = 0 , 0 
        for i in range(l):
            a , b = nums1[i], nums2[i]
            if a == b:
                continue
            x = abs(a-b)
            sum += x

            # 二分查找
            left , right = 0 , l
            while left < right:
                mid = left + (right - left) //2 
                if nums1_clone[mid] <= b:
                    left = mid + 1
                else:
                    right = mid
            
            nd = abs(nums1_clone[right] - b)
            if right + 1 < l:
                nd = min(nd,abs(nums1_clone[right+1]-b))
            if nd < x:
                max_value = max(max_value,x-nd)
        return (sum-max_value)% (10**9 + 7)

s = Solution()
print(s.minAbsoluteSumDiff([1,10,4,4,2,7],[9,3,5,1,7,4]))
