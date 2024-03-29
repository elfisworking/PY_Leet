from typing import List 
class UnionFind:
    def __init__(self,n:int):
        self.parent = list(range(n))
        self.size = [1]* n
        self.n = n
        self.setCount = n
    def findSet(self,x:int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]
    
    def unite(self,x:int,y:int) -> bool:
        x , y = self.findSet(x) , self.findSet(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y ,x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    def connected(self,x:int,y:int)->bool:
        x , y = self.findSet(x),self.findSet(y)
        return x==y
class Solution:
    def minimumEffortPath(self,heights:List[List[int]])->int:
        m,n = len(heights),len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i>0:
                    edges.append((iden-n,iden,abs(heights[i][j]-heights[i-1][j])))
                if j > 0:
                    edges.append((iden-1,iden,abs(heights[i][j]-heights[i][j-1])))
        
        edges.sort(key=lambda e:e[2])
        uf = UnionFind(m*n)
        ans = 0
        for x ,y ,v in edges:
            uf.unite(x,y)
            if uf.connected(0,m*n-1):
                ans = v
                break
        return ans