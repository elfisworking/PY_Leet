from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        l = len(A)
        # 单调递增
        flag1 = True
        flag2 = True 
        for i in range(l-1):
            if A[i]>A[i+1]:
                flag1 = False
            if A[i]<A[i+1]:
                flag2 = False
        return flag2 or flag1