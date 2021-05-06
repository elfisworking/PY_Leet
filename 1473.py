# 粉刷房子 III
# https://leetcode-cn.com/problems/paint-house-iii/
from typing import List
from functools import lru_cache
# 本题使用了动态规划的解题思路
# 思考 暴力搜索，搜索+记忆，动态规划
# 动态规划 转移方程
class Solution:
    # 搜索+记忆
    def minCost_DFS(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dfs(i, target, color):
            if target == -1 or i + target > m:
                return float("inf")
            if i == m:
                return 0

            if houses[i] != 0:
                return dfs(i+1, target if houses[i]==color else target-1, houses[i])
            else:
                return min(dfs(i+1, target if j+1==color else target-1, j+1) + cost[i][j] for j in range(n))

        ans = dfs(0, target, -1)
        return ans if ans != float("inf") else -1
    # 动规的方法
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float("inf")
        # dp[i][j][k]
        dp = [[[0]*(target+1) for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                dp[i][j][0] = INF
        # k表示分区
        # i表示前i个房子
        # j表示颜色
        for i in range(1,m+1):
            # 判断当前房子的颜色情况
            color = houses[i-1]
            for j in range(1,n+1):
                for k in range(1,target+1):
                    # 此处做优化 此时已经明显不可能了
                    if k > i:
                        dp[i][j][k] = INF
                        continue
                    if color!=0 : #表示已经上色
                        if j == color:
                            tmp = INF
                            for p in range(1,n+1):
                                if p != j:
                                    tmp = min(tmp,dp[i-1][p][k-1])
                            # 此时不需要加cost 
                            dp[i][j][k] = min(dp[i-1][j][k],tmp)
                        else:
                            dp[i][j][k] = INF
                    else:
                        u = cost[i-1][j-1]
                        tmp = INF
                        # 形成分区的最优情况
                        for p in range(1,n+1):
                            if p!=j :
                                tmp = min(tmp,dp[i-1][p][k-1])
                        # 判断不分区和分区的情况下 哪个值更小
                        dp[i][j][k] = min(dp[i-1][j][k],tmp)+u
        res = INF
        for i in range(1,n+1):
            res = min(res,dp[m][i][target])
        return -1 if res == INF else res