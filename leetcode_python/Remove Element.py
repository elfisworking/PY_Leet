from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                if left != i:
                    nums[left] = nums[i]
                left +=1
        return left
s = Solution()
print(s.removeElement([1,1,0,1],0))