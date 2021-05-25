# 75. 颜色分类
# https://leetcode-cn.com/problems/sort-colors/
from typing import List
class Solution:
    def sortColors_one_pointer(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 可以直接对其进行排序
        # nums.sort()
        # 单指针的方法
        # 还可以使用hash表，统计每一个数的数量，然后覆盖 不过这需要两次循环
        # 除了单指针，我们还可以使用双指针
        ptr = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                nums[ptr] , nums[i] = nums[i] , nums[ptr]
                ptr += 1
        for i in range(ptr,l):
            if nums[i] == 1:
                nums[ptr] , nums[i] = nums[i] , nums[ptr]
                ptr += 1
        
        # 双指针的方法
        def sortColors_two_pointer(self, nums: List[int]) -> None:
            pass