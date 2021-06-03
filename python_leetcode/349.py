# 349. 两个数组的交集
# https://leetcode-cn.com/problems/intersection-of-two-arrays/
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for a in nums1:
            if a in nums2:
                res.append(a)
        return res
    # 排序 双指针
    def intersection_two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = set()
        while i< len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.add(nums1[i])
                i += 1
                j += 1
        return list(res)