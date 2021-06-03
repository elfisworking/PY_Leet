from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 感觉使用快慢指针
        l = len(nums)
        if l < 2:
            return l
        left = right = 2
        while right < l:
            if nums[left-2] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
