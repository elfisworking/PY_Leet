from typing import List
class Solution:
    # 错误的解法
    # def trap(self, height: List[int]) -> int:
    #     l  = len(height)
    #     if l == 0:
    #         return 0
    #     left , right = 0, 0
    #     while  left<l and height[left]==0 :
    #         left += 1
    #     if left==l:
    #         return 0
    #     right = left+1
    #     ans = 0
    #     while right<l and left<l:
    #         while  right<l and height[right]<height[left] :
    #             right += 1
    #         if right==l:
    #             left +=1
    #             right = left+1
    #         else:
    #             ans += min(height[left],height[right])*(right-left-1)-sum(height[left+1:right])
    #             left = right
    #             right = left+1
    #     return ans
    # 暴力方法 超出时间限制 
    def trap_violent_solution(self, height: List[int]) -> int:
        l = len(height)
        if l <= 0:
            return 0
        ans = 0
        for i in range(1,l-1):
            max_left , max_right = 0 ,0 
            # 向左边探索
            for a in range(i,-1,-1):
                max_left = max(max_left,height[a])
            # 向右边探索
            for b in range(i,l):
                max_right = max(max_right,height[b])
            ans += min(max_left,max_right)-height[i]
        return ans
    # 使用动态规划
    def trap(self, height: List[int]) -> int:


s = Solution()
print(s.trap([4,2,0,3,2,5]))
            

      