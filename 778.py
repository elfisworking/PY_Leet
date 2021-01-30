from typing import List
# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        edge = list()
        m , n = len(grid),len(grid[0])
        for a in range(m):
            for b in range(n):
                iden = m*a + b
                if a>0 :
                    edge.append((iden-m,iden,max(grid[a-1][b],grid[a][b])))
                if b>0 :
                    edge.append((iden-1,iden,max(grid[a][b-1],grid[a][b])))
        
        edge.sort(key=lambda e:e[2])
        uf = UnionFind(m*n)
        ans = 0 
        for x, y ,u in edge:
            uf.unite(x,y)
            if uf.connected(0,m*n-1):
                ans = u
                break
        return ans
s = Solution()
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))