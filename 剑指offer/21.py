# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 双指针问题
        if not nums:
            return []
        left , right = 0 ,len(nums)-1
        while left < right:
            while left<right and nums[left]%2 == 1 :
                left += 1
            while  left < right and  nums[right]%2 == 0:
                right -= 1
            if left < right:
                nums[left] , nums[right] = nums[right],nums[left]
        return nums
