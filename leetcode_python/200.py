# 200. 岛屿数量
# https://leetcode-cn.com/problems/number-of-islands/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 200.py
@Time : 2022/04/02 23:12:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class UnionSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, i, j):
        i, j = self.find(self.parent[i]), self.find(self.parent[j])
        if i == j:
            return 
        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j
            if self.rank[i] == self.rank[j]:
                self.rank[j] += 1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        unionset = UnionSet(m * n)
        direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    unionset.parent[n * i + j] = -1
                    continue
                for a, b in direction:
                    new_i = i + a
                    new_j = j + b
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1":
                        unionset.union(n * i + j, n * new_i + new_j)
        
        ans = 0
        print(unionset.parent)
        for index,val in enumerate(unionset.parent):
            if index == val and val != -1:
                ans += 1
        return ans
