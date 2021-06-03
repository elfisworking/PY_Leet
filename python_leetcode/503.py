from typing import List
class Solution:
    # 暴力方法
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     ans = list()
    #     l = len(nums)
    #     for i in range(l):
    #         flag = True
    #         for a in range(i+1,l):
    #             if nums[a]>nums[i]:
    #                 ans.append(nums[a])
    #                 flag = False
    #                 break
    #         if flag:
    #             for a in range(i):
    #                 if nums[a]>nums[i]:
    #                     ans.append(nums[a])
    #                     flag = False
    #                     break
    #         if flag:
    #             ans.append(-1)
            
    #     return ans

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res