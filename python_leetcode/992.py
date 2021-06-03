from typing import List
import collections
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A,K)-self.atMostK(A,K-1)
    def atMostK(self, A, K):
        N = len(A)
        left, right = 0, 0
        counter = collections.Counter()
        distinct = 0
        res = 0
        while right < N:
            if counter[A[right]] == 0:
                distinct += 1
            counter[A[right]] += 1
            while distinct > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    distinct -= 1
                left += 1
            res += right - left + 1
            right += 1
        return res
s = Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3],2))