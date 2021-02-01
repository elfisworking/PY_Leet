from typing import List
class Solution:
    # 使用回溯的方法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        l = len(nums)
        def dep(temp=[],index=0):
            for i in range(index,l):
                temp.append(nums[i])
                ans.append(temp[:])
                dep(temp,i+1)
                temp.pop()
        dep()
        return ans
    # 使用的集合的方式
    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            ans += [j+[i] for j in ans]
        return ans

s =Solution()
print(s.subsets_1([1,2,3]))