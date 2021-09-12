from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left , right = 0 , 0
        mutli_res = 1
        res = 0
        while right < len(nums):
            mutli_res *= nums[right]
            while mutli_res >= k and left <= right:
                mutli_res /= nums[left]
                left += 1
            res += right - left + 1
            right += 1 
        return res
s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))