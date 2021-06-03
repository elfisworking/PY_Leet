from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        N = len(A)
        res = 0 
        left , right  = 0 , 0 
        zeros = 0
        while right < N :
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res,right - left + 1)
            right += 1
        return res
    # 上文中我们记录了每一次的的窗口大小 其实没有必要只要记录最大的就行了
    def longestOnes_1(self, A: List[int], K: int) -> int:
        left,right,count = 0,0,0       #本来定义了max_len用来实时记录窗口大小，但后来发现非必要,因为窗口大小没有变小
        for right in range(len(A)):
            if A[right] == 0:
                count += 1
            if count > K:
                if A[left] == 0:
                    count -= 1
                left += 1
        return right-left+1