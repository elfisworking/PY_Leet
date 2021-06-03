from typing import List
# 45. 跳跃游戏 II
# https://leetcode-cn.com/problems/jump-game-ii/
class Solution:
    # 正向的方法
    def jump(self, nums: List[int]) -> int:
        end  = 0
        i = 0
        endLocation = 0
        step = 0
        for i in range(len(nums)-1): # 注意这里面的len(nums)-1 不是len(nums) 是为了避免当end为终点时，step额外加一的情况
            endLocation = max(endLocation,i+nums[i])
            if i == end:
                end = endLocation
                step += 1
        return step