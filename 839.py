from typing import List
# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, node: int) -> int:
        # if self.parent[x] == x:
        #     return x
        # self.parent[x] = self.findset(self.parent[x])
        # return self.parent[x]
        while self.parent[node] != node:
            node = self.parent[self.parent[node]]
               
        return node
    
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
    # 一开始的时间复杂度是由这个引起的
    # def isSimilar(self, str1, str2):
    #     count = 0
    #     for i in range(len(str1)):
    #         if str1[i] != str2[i]:
    #             count += 1
    #     return count == 2 or count == 0
    # 换成这个函数以后 时间花费由2084ms减少到232ms
    def check(self,a: str, b: str) -> bool:
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True
    def numSimilarGroups(self, strs: List[str]) -> int:
        m = len(strs)
        uf =UnionFind(m)
        for a in range(m):
            for b in range(a+1,m):
                if self.check(strs[a],strs[b]):
                    uf.unite(a,b)
        return uf.setCount

s =Solution()
print(s.numSimilarGroups(["omv","ovm"]))
