from typing import List
# class Solution:
#     # 动态规划方式
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m , n  = len(grid),len(grid[0])
#         l = m*n
#         arr = [0]*l
#         arr[0] = grid[0][0]
#         for a in range(m):
#             for b in range(n):
#                 if a>0 and b >0 :
#                   arr[a*n+b]=grid[a][b]+min(arr[(a-1)*n+b],arr[a*n+b-1])
#                 elif a ==0 and b>0 :
#                     arr[a*n+b]=grid[a][b]+arr[a*n+b-1]
#                 elif b==0 and a>0:
#                     arr[a*n+b]=grid[a][b]+arr[(a-1)*n+b]
#         return arr[l-1]

# 2021.9.25 re-code
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        dp = [ [0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[m-1][n-1]
        

s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]]))