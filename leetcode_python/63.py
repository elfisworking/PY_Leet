# 63. 不同路径 II
# https://leetcode-cn.com/problems/unique-paths-ii/
from typing import List
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [ [0 for _ in range(n)] for _ in range(m)]
#         # 不能直接将dp[0][0]设为1  要考虑到有障碍物的情况
#         if obstacleGrid[0][0] == 1:
#             dp[0][0] = 0
#         else:
#             dp[0][0] = 1
#         for i in range(1,n):
#             if obstacleGrid[0][i] != 1:
#                 dp[0][i] = dp[0][i-1]
#         for i in range(1,m):
#             if obstacleGrid[i][0] != 1:
#                 dp[i][0] = dp[i-1][0]
#         for a in range(1,m):
#             for b in range(1,n):
#                 if obstacleGrid[a][b] != 1:
#                     dp[a][b] = dp[a-1][b] + dp[a][b-1]
#         return dp[m-1][n-1]
# 2021.9.25 re-code
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if obstacleGrid[i][j] != 1 and j > 0:
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j] !=1 and i > 0:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return  dp[m-1][n-1]
s = Solution()