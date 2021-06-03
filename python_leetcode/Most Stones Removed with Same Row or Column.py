from typing import List
class Solution:
    # 没有优化的版本
    def removeStones(self, stones: List[List[int]]) -> int:
        l = len(stones)
        parent = list(range(l))
        def find_parent(x):
            if  parent[x] ==x :
                return parent[x]
            else:
                return find_parent(parent[x])

        def union(x,y):
            parent[find_parent(x)] = find_parent(y)
        
        for i in range(l):
            for j in range(i+1,l):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        
        res = 0
        for i in range(l):
            if parent[i] != i:
                res = res + 1
        return res

class Solution_1:
    def init_tree(self,n):
        self.fa = [i for i in range(n)]
    
    def find(self,x):
        while self.fa[x]!=x:
            x= self.fa[x]
        return x

    def union(self,u,v):
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            return 
        self.fa[ru] = rv
        return 

    def removeStones(self, stones: List[List[int]]) -> int:
        self.init_tree(8)
        for x,y in stones:
            self.union(x,y+4)  # 并查集是一维的，比如第二行和第二列可能难以区分，故将列+10000转换为一维的
        print(self.fa)
        print(len({self.find(x) for x,y in stones}))
        return len(stones)-len({self.find(y+4) for x,y in stones}) # {}表示集合，自动去重
        
s = Solution_1()
print(s.removeStones([[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]]))