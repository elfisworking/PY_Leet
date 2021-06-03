# 1040. 移动石子直到连续 II
# https://leetcode-cn.com/problems/moving-stones-until-consecutive-ii/
# 输入：[7,4,9]
# 输出：[1,2]
# 解释：
# 我们可以移动一次，4 -> 8，游戏结束。
# 或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。
# 这个最大值是怎么来的???
from typing import List
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        inter_space = stones[-1] - stones[0] + 1 - n

        max_ = inter_space - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)
                #主要卡第一步，因为必须交叉着进行  以后的步骤，都可以想办法，每次范围只缩小1
        min_ = max_
        R = 0
        for L in range(n):  
            while R + 1 < n and stones[R+1] - stones[L] + 1 <= n:   #维护一个长度为n的窗口
                R += 1
            cost = n - (R - L + 1)          #窗口内的空格的个数

            if R-L+1 == n-1 and stones[R]-stones[L]+1 == n-1:       #示例2： 3 4 5 6 10，最少操作数不是1，是2
                cost = 2
            
            min_ = min(min_, cost)
        
        return [min_, max_]
        