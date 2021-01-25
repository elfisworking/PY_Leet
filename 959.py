from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        parent = [i for i in range(4*N*N)]

        def find(node):
            if parent[node] != node:
               parent[node] = find(parent[node])
            return parent[node]

        def union(a,b):
            root_a,root_b = find(a),find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        for r in range(N):
            for c in range(N):
                base = 4 * (r * N + c)
                char = grid[r][c]
                # 根据三种不同情况链接四个子块
                if char == '\\':
                    union(base + 0,base + 3)
                    union(base + 1,base + 2)
                elif char == '/':
                    union(base + 0,base + 1)
                    union(base + 2,base + 3)
                else:
                    union(base + 0,base + 1)
                    union(base + 2,base + 3)
                    union(base + 0,base + 2)
                # 若该快右边/下面还有块则连接相应子块
                if c < N-1: union(base + 2,base + 4)
                if r < N-1: union(base + 3,base + 4*N + 1)
        return sum(parent[i] == i for i in range(4*N*N))
