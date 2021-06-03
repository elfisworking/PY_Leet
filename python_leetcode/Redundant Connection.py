class Solution:
    # 并查集思想
    def findRedundantConnection(self, edges):
        l = len(edges)
        parent = list(range(l+1))
        def find_parent(x):
            if parent[x] == x:
                return parent[x]
            else:
                return find_parent(parent[x])
        def union(x,y):
            parent[x] = y
        for node1, node2 in edges:
            parent_1 = find_parent(node1)
            parent_2 = find_parent(node2)
            if parent_1 != parent_2:
                union(parent_1,parent_2)
            else:
                return [node1,node2]
        return []
s = Solution()
print(s.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
        