# 1049. 最后一块石头的重量 II
# https://leetcode-cn.com/problems/last-stone-weight-ii/
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n , m = len(stones), total//2
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(m+1):
                if j < stones[i]:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] or dp[i][j-stones[i]]
        
        ans = None
        for j in range(m,-1,-1):
            if dp[n][j]:
                ans = total-2*j
                break
        return ans

s = Solution()
print(s.lastStoneWeightII([2,7,4,1,8,1]))
        