# 810. 黑板异或游戏
# https://leetcode-cn.com/problems/chalkboard-xor-game/
# 涉及了博弈论
from typing import List
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums)%2:
            k = 0
            for i in nums:
                k = k^i

            if k:
                return False
        
        return True