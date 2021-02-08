from typing import List
class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     l = len(nums)
    #     left, right = 0,k
    #     s = sum(nums[left:k])
    #     while right<l:
    #         if nums[right] > nums[left]:
    #             s = max(s,sum(nums[left+1:right+1]))
    #         right += 1
    #         left += 1
    #     return s/k
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:return nums[0]
        SET = sum(nums[:k])  
        cnt = 0
        maxx = SET
        for num in range(k,len(nums)):
            SET -= nums[cnt]
            SET += nums[num]
            cnt += 1
            if SET > maxx:
                maxx = SET 
        return maxx/k


s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3],4))
            