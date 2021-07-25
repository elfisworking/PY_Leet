# 剑指 Offer 53 - I. 在排序数组中查找数字 I
# https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 53-1.py
@Time : 2021/07/25 21:26:47
@Author : YuMin Zhang
@Thinking : 时间复杂度可以是O(n)即一次遍历，但是也可以用二分的思想将时间复杂度将为O(logn) 
'''
class Solution:
    # # 一次遍历
    # def search(self, nums: List[int], target: int) -> int:
    #     count = 0
    #     for i in nums:
    #         if i == target:
    #             count += 1
    #         elif i > target:
    #             break
    #     return count
    # 用二分的思想
    def search(self, nums: List[int], target: int) -> int:
        if not nums or nums[-1] < target or nums[0] > target:
            return 0
        l = len(nums)
        left , right = 0 ,l 
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return 0
        
        count = 0
        for i in range(left,l):
            if nums[i] == target:
                count += 1
            elif nums[i] > target:
                break
        return count
s = Solution()
print(s.search([5,7,7,8,8,10],6))