# 1020. 飞地的数量
# https://leetcode-cn.com/problems/number-of-enclaves/
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(x,y):
            if not grid[x][y]:
                return None
            else:
                grid[x][y] = 0
            if x < n-1:
                dfs(x+1,y)
            if x > 0:
                dfs(x-1,y)
            if y < m-1:
                dfs(x,y+1)
            if y > 0:
                dfs(x,y-1)
        
        # 从四个边开始探索
        for i in range(n):
            if grid[i][0]:
                dfs(i,0)
            if grid[i][m-1]:
                dfs(i,m-1)
		
        for j in range(m):
            if grid[0][j]:
                dfs(0,j)
            if grid[n - 1][j]:
                dfs(n - 1,j)
        
        ans = 0
        for i in range(1, n - 1):
	        ans += sum(grid[i])
        return ans