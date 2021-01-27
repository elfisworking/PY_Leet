from typing import List
class Solution:
    # 时间耗时 68ms 这个思想是从重点向后跳 看能否会跳到重点 
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True
        step =[i for i in range(l-1,0,-1)]
        def jump(nums,sub,length):
            if length == 2:
                if nums[0]>=1:
                    return True
                return False
            flag = False
            for i in range(length-2,-1,-1):
                if nums[i] >= step[i]-sub:
                    nums.pop()
                    sub +=1
                    flag  = jump(nums,sub,length-1)
                    break
            return flag
        return jump(nums,0,l)
    # 这个思想是贪心思想 从起点向前跳 实时维护一个最远距离
    # 时间耗时56秒
    # 官方解法
    def canJump_offical(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
    # 解答中最快的解法
    # 时间耗时 40ms
    def canJump_1(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        k = 1
        u = 1
        l = len(nums)
        for i in nums:

            k -= 1
            if i > k:
                k = i
            if k == 0 and u != l:
                return False
            u += 1
        
        return True
s = Solution()
print(s.canJump_1([2,3,1,0,4]))