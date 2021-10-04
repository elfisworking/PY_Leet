
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : topological_sort.py
@Time : 2021/09/26 10:38:53
@Author : YuMin Zhang
'''
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        
        stack.append(v)
    
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i,visited,stack)
        
        print(stack[::-1])

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(0, 5)
g.add_edge(0, 4)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort()
