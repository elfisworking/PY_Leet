from typing import List
class Solution:
    # 动态规划方式
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n  = len(grid),len(grid[0])
        l = m*n
        arr = [0]*l
        arr[0] = grid[0][0]
        for a in range(m):
            for b in range(n):
                if a>0 and b >0 :
                  arr[a*n+b]=grid[a][b]+min(arr[(a-1)*n+b],arr[a*n+b-1])
                elif a ==0 and b>0 :
                    arr[a*n+b]=grid[a][b]+arr[a*n+b-1]
                elif b==0 and a>0:
                    arr[a*n+b]=grid[a][b]+arr[(a-1)*n+b]
        return arr[l-1]
s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]]))