# 2045. 到达目的地的第二短时间
# https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination/
from curses.ascii import SO
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2045.py
@Time : 2022/01/24 11:26:13
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Hard
'''
# class Solution:
#     def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
#         g = defaultdict(list)
#         for edge in edges:
#             g[edge[0]].append(edge[1])
#             g[edge[1]].append(edge[0])
#         times = set()
#         visited = [0] * (n + 1)
#         visited[0] = 1
#         visited[1] = 1
#         def dfs(location, t):
#             if location == n:
#                 times.add(t)
#                 return 
#             remainder = t % change
#             if (t // change) % 2 == 1:
#                 t += (change - remainder)
#             for i in g[location]:
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     dfs(i, t + time)
#                     visited[i] = 0
#         dfs(1, 0)
#         times = list(times)
#         times.sort()
#         return times[1]
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for e in edges:
            x, y = e[0], e[1]
            graph[x].append(y)
            graph[y].append(x)

        # dist[i][0] 表示从 1 到 i 的最短路长度，dist[i][1] 表示从 1 到 i 的严格次短路长度
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        q = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            p = q.popleft()
            for y in graph[p[0]]:
                d = p[1] + 1
                if d < dist[y][0]:
                    dist[y][0] = d
                    q.append((y, d))
                elif dist[y][0] < d < dist[y][1]:
                    dist[y][1] = d
                    q.append((y, d))

        ans = 0
        for _ in range(dist[n][1]):
            if ans % (change * 2) >= change:
                ans += change * 2 - ans % (change * 2)
            ans += time
        return ans
s = Solution()
print(s.secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))