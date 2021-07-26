#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 57.py
@Time : 2021/07/26 14:28:20
@Author : YuMin Zhang
@State : Independent
@Thinking : 除了可以使用哈希表，还可以使用双指针的方法，考虑到这是一个有序的数组
'''
class Solution:
    # 哈希表
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     d = defaultdict(int)
    #     for i in nums:
    #         a = target - i 
    #         if a in d:
    #             return [a,i]
    #         else:
    #             d[i] = a
    #     return []

    # 双指针
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     left , right = 0 , len(nums)-1
    #     while left < right:
    #         sum = nums[left] + nums[right]
    #         if sum > target:
    #             right -= 1
    #         elif sum < target:
    #             left += 1
    #         else:
    #             return [nums[left],nums[right]]
    #     return []
    
    # 可以使用二分法对双指针进行优化

s = Solution()
print(s.twoSum([2,7,11,15],9))
                