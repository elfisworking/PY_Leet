from typing import List
class Solution:
    # 使用了额外空间的做法
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        l = len(nums)
        h = [0]*l
        ans = []
        for v in nums:
            h[v-1] = 1
        for i in range(l) :
            if h[i] == 0:
                ans.append(i+1)
        return ans
    # 使用原来的数组来做hash数组 这里使用的是加法
    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for v in nums:
            x = (v-1)%l
            nums[x] += l
        ans = [i+1 for i , val in enumerate(nums) if val < l]
        return ans
    # 这里也是使用原数组进行hash  不过这里使用的是正负号
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(len(nums)):
            newIndex = abs(nums[i]) - 1
            if nums[newIndex] > 0:
                nums[newIndex] *= -1
        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j + 1)
        return res
s = Solution()
print(s.findDisappearedNumbers([1,1]))
