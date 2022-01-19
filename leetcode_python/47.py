from typing  import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        l = len(nums)
        def dfs(begin):
            if len(temp) == l:
                ans.append(temp[:])
                return
            repetition = set() # important
            for i in range(begin,l):  
                if nums[i] not in repetition:
                    repetition.add(nums[i])
                else:
                    continue
                temp.append(nums[i])
                nums[begin],nums[i] = nums[i],nums[begin]
                dfs(begin+1)
                nums[begin],nums[i] = nums[i],nums[begin]
                temp.pop()
        dfs(0)
        return ans
s = Solution()
print(s.permute([1,2,1]))

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        
        self.backtrack([], nums, check)
        return self.res
        
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            check[i] = 0
