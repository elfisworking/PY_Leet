# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        # self.n = n
        # # 当前连通分量数目
        # self.setCount = n
    # 修改后的find函数 减少花费的时间
    def findset(self, x: int) -> int:
        # 进行了路径压缩
        # if self.parent[x] == x:
        #     return x
        # self.parent[x] = self.findset(self.parent[x])
        # return self.parent[x]

        # 这是一种非递归的寻找root的方式，但是并没有进行路径压缩
        # while self.parent[node] != node:
        #     node = self.parent[self.parent[node]]  
        # return node
        
        return x if self.parent[x] == x else (self.parent[x] = self.findset(self.parent[x]))
    
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        #  按 秩合并
        if self.rank[x] < self.rank[y]:
            self.parent[x] == y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y
