from typing import List
# 思路：排序 考虑负数的情况 如果有负数 要考虑最小的两个负数相乘 然后乘以最大额度整数的情况
# 可以使用max()函数对两者直接进行比较
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        else:
            nums.sort()
            return max(nums[-1] * nums[-2] * nums[-3],nums[0]*nums[1]*nums[-1])
        