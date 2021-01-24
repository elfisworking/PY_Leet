from typing import List
class Solution:
    # ordinary method
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(1,l+2):
            if i not in nums:
                return i
class Solution_1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1

s = Solution()
print(s.firstMissingPositive([7,8,9,11,12]))