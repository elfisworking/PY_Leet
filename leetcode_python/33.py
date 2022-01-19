from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# error 
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             if target >= nums[0]:
#                 if nums[left] <= nums[mid] <= nums[right]:
#                     if nums[mid] > target:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
#                 else:
#                     right = mid - 1
#             else:
#                 if nums[left] <= nums[mid] <= nums[right]:
#                     if nums[mid] > target:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
#                 else:
#                     left = mid + 1
#         return -1
    
                     
S = Solution()
print(S.search([4,5,0,1,2],5))
            