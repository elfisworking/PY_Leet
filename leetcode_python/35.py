from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        l = len(nums)
        if target > nums[l-1]:
            return l
        right = l-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid 
            else:
                left =  mid+1 
        return left
s =  Solution()
print(s.searchInsert([1, 2, 3, 3], 3))