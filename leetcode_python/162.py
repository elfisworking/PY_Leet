# 162. 寻找峰值
# https://leetcode-cn.com/problems/find-peak-element/
from typing import List
class Solution:
    # 暴力解法  O(n)
    def findPeakElement_burst(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1 :
            return 0
        if nums[0]>nums[1]:
            return 0
        for i in range(1,l-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i
        if nums[-1]>nums[-2]:
            return l-1
        return 0
    # 十分的巧妙 好好的想想  局部空间的递增和递减 缩小范围
    def findPeakElement_binary_search(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left