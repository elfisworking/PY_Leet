# 787. K 站中转内最便宜的航班
# https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
from typing import List
from collections import defaultdict
class Solution:
#     # 超时
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         d = defaultdict(list)
#         visited= [-1]*n
#         for i in flights:
#             d[i[0]].append([i[1],i[2]])
        
#         res = -1
#         def dfs(node,current_price,jump):
#             if jump > k+1:
#                 return 
#             nonlocal res
#             if visited[node] != -1 and visited[node] < current_price:
#                 return 
#             if res != -1 and res < current_price:
#                 return 
#             if node == dst:
#                 if res == -1:
#                     res = current_price
#                 else:
#                     res = min(res,current_price)
#                 return 
#             for i in d[node]:
#                 dfs(i[0],current_price+i[1],jump+1)
        
#         dfs(src,0,0)
#         return res
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 建个哈希表，方便查找起到到终点的cost
        flight_map = defaultdict(list)
        for fro, to, price in flights:
            flight_map[fro].append((to, price))

        level = 0
        # 建一个visited数组，初始化为无穷大
        # 存储已经访问过的节点，及其cost，如果已经被访问过，但是遇到cost更低的，可以继续进入
        visited = [float('inf')] * n
        min_cost = float('inf')

        # 存 起点 的当前的 cost
        queue = deque([(src, 0)])
        # 注意 k+1 条边 = k 个中转站
        while queue and level <= k+1:
            queue_len = len(queue)

            for _ in range(queue_len):
                curr, cost = queue.popleft()
                if cost != 0:
                    visited[curr] = cost

                if curr == dst:
                    min_cost = min(cost, min_cost)
                else:
                    next_flights = flight_map[curr]
                    for next_to, next_cost in next_flights:
                        # 不要重复访问一些节点，或者更差的结果就直接剪掉
                        if next_cost + cost < visited[next_to]:
                            queue.append((next_to, cost + next_cost))
            level += 1

        return min_cost if min_cost != float('inf') else -1

s = Solution()
print(s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
