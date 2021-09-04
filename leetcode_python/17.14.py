import heapq
from typing import List
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        res = []
        for i in range(k):
            heapq.heappush(res,-arr[i])
        
        l = len(arr)
        for i in range(k,l):
            heapq.heappushpop(res,-arr[i])
        
        res = [ -i for i in res]
        return res