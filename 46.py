from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        l = len(nums)
        def dfs(begin):
            if len(temp) == l:
                ans.append(temp[:])
                return
            for i in range(begin,l):    
                temp.append(nums[i])
                nums[begin],nums[i] = nums[i],nums[begin]
                dfs(begin+1)
                nums[begin],nums[i] = nums[i],nums[begin]
                temp.pop()
        dfs(0)
        return ans
s = Solution()
print(s.permute([1,2,3]))