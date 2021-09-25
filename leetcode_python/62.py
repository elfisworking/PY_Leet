# 62. 不同路径
# https://leetcode-cn.com/problems/unique-paths/
# class Solution:
#     # 简单的动规
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = 1
#         for a in range(m):
#             for b in range(n):
#                 if a==0 and b== 0:
#                     continue
#                 elif  a != 0  and b==0:
#                     dp[a][b] = dp[a-1][b]
#                 elif   a == 0 and b != 0:
#                     dp[a][b] = dp[a][b-1]
#                 else:
#                     dp[a][b] = dp[a][b-1]+dp[a-1][b]
#         return dp[m-1][n-1]

# 2021.9.25 re-code
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
s = Solution()
print(s.uniquePaths(3,7))