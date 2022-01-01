# 912. 排序数组
# https://leetcode-cn.com/problems/sort-an-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 912.py
@Time : 2022/01/01 16:21:12
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right: return 
        mid = self.partition(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)
    
    def partition(self, nums, left, right):
        pivot = randint(left, right) # 随机是必须的要不然超时
        nums[pivot], nums[right] = nums[right], nums[pivot]
        tmp = nums[right]
        fast = left
        slow = left - 1
        while fast < right:
            if nums[fast] <= tmp:
                slow += 1
                nums[slow] , nums[fast] = nums[fast], nums[slow]
            fast += 1
        nums[slow + 1], nums[right] = nums[right], nums[slow + 1]
        return slow + 1
s = Solution()
print(s.sortArray([5,2,3,1]))