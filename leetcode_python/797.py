# 797. 所有可能的路径
# https://leetcode-cn.com/problems/all-paths-from-source-to-target/
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) -1 
        d = dict()
        for index, value in enumerate(graph):
            d[index] = value
        res = []
        def dfs(index:int,path:list,n):
            if index == n:
                res.append(path)
                return 
            for node in d[index]:
                dfs(node,path + [node],n)
        
        dfs(0,[0],n)
        return res

s = Solution()
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))