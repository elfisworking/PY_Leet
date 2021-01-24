from typing import List
class Solution:
    # 这个时间复杂度太高了 
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        parent = [i for i in range(n)]
        # 不要使用递归 可以大大减少时间复杂度
        def find_parent(x):
            if parent[x] == x:
                return x
            return find_parent(parent[x])
        def union(x,y):
            parent[x] = y
        for line in connections:
            x = find_parent(line[0])
            y = find_parent(line[1])
            if x != y:
                union(x,y)
        set = {find_parent(i) for i in parent}
        return  len(set) -1 

    def makeConnected_1(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent, res = list(range(n)), 0

        def find_root(node):
            while parent[node] != node:
                node = parent[parent[node]]
               
            return node

        for x, y in connections:
            r1 = find_root(x)
            r2 = find_root(y)
            if r1 == r2:
                # 这是冗余的线
                res += 1
                continue
            parent[r1] = r2

        return res - (len(connections) - n + 1)

s = Solution()
print(s.makeConnected_1(4,[[0,1],[0,2],[1,2]]))