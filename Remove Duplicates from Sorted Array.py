from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[res] = nums[i+1]
                res +=1
        return res
s =Solution()
print(s.removeDuplicates([1,1,2,2,3,3,3,3,4]))