from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0,len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid]==nums[right]:
                right = right -1
            
        return nums[left]
s = Solution()
print(s.findMin([3,1,1]))