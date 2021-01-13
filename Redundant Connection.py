class Solution:
    # 并查集思想
    def findRedundantConnection(self, edges):
        
        treeSet = set()
        for val in edges:
            if val[0] in treeSet and val[1] in treeSet:
                return val
            else:
                treeSet.add(val[0])
                treeSet.add(val[1])
s = Solution()
print(s.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
        