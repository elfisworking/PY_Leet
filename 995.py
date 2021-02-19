from typing import List
import collections
class Solution:
    # 使用滑动窗口的方法
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        que = collections.deque()
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i+K > N :
                    return -1
                que.append(i)
                res += 1
        return res
    # 模拟翻转
    def minKBitFlips_1(self, A, K):
        N = len(A)
        res = 0
        for i in range(N-K+1):
            if A[i] == 1:
                continue
            for j in range(K):
                A[i+j] ^= 1
            res += 1
        for i  in range (N):
            if A[i] == 0:
                return -1
        return res
    # 差分数组
    def minKBitFlips_2(self, A, K):
        N = len(A)
        diff = [0]*(N+1)
        ans = 0
        revCnt = 0
        for i in range(N):
            revCnt += diff[i]
            if (A[i]+revCnt)% 2 == 0:
                if i+ K > N:
                    return -1
                ans += 1
                revCnt += 1
                diff[i+K] -= 1
        return ans



