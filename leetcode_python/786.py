# 786. 第 K 个最小的素数分数
# https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 786.py
@Time : 2021/11/29 15:01:37
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    # max heap and dict. bad solution
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        d = defaultdict(list)
        heap = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                div = arr[i] / arr[j]
                d[div] = [arr[i], arr[j]]
                if len(heap) == k:
                    heapq.heappush(heap, -div)
                    heapq.heappop(heap)
                else:
                    heapq.heappush(heap, -div)
        return d[-heap[0]]


class Solution:
    # 多路归并
    def kthSmallestPrimeFraction(self, A: List[int], k: int) -> List[int]:
        q = [(A[0]/A[i], 0 , i) for i in range(1,len(A))]
        heapq.heapify(q)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(q)
            if i + 1 < j:
                heapq.heappush(q, (A[i + 1] / A[j], i + 1, j))
        return [ A[ q[0][1] ], A[ q[0][2] ] ]