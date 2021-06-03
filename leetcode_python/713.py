# 713. 乘积小于K的子数组
# https://leetcode-cn.com/problems/subarray-product-less-than-k/
from  typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left , right = 0 , 0
        mul = 1
        res = 0
        while right < len(nums):
            mul *= nums[right]
            while mul >=k and left <= right:
                mul /=nums[left]
                left += 1
            res += right -left + 1
            right += 1
        return res