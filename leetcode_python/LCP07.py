# LCP 07. 传递信息
# https://leetcode-cn.com/problems/chuan-di-xin-xi/
from typing import List
from collections import defaultdict
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        ans = [0]
        relation_dict = defaultdict(list)
        
        for i in relation:
            relation_dict[i[0]].append(i[1])
        
        def dfs(gamer,depth):
            relations = relation_dict[gamer]     
            for g in relations:
                if depth == k:
                    if g == n-1:
                        ans[0] += 1
                else:
                    dfs(g,depth+1)
        dfs(0,1)
        return ans[0]