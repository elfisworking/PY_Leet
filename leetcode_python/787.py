# 787. K 站中转内最便宜的航班
# https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
from typing import List
from collections import defaultdict
class Solution:
    # 超时
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #     d = defaultdict(list)
        
    #     for i in flights:
    #         d[i[0]].append([i[1],i[2]])
        
    #     res = -1
    #     def dfs(node,current_price,jump):
    #         if jump > k+1:
    #             return 
    #         nonlocal res 
    #         if res != -1 and res < current_price:
    #             return 
    #         if node == dst:
    #             if res == -1:
    #                 res = current_price
    #             else:
    #                 res = min(res,current_price)
    #             return 
    #         for i in d[node]:
    #             dfs(i[0],current_price+i[1],jump+1)
        
    #     dfs(src,0,0)
    #     return res
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
s = Solution()
print(s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
