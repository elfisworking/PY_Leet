# https://leetcode-cn.com/problems/binary-search/
# 704. 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                mid = mid - 1
            else : 
                mid = mid + 1
        
        return -1