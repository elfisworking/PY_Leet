# 找出第 K 大的异或坐标值
# https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/
from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        ans.append(matrix[0][0])
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for a in range(0,row):
            dp[a][0] = matrix[a][0]
        for a in range(0,row):
            for b in range(1,col):
                dp[a][b] = dp[a][b-1]^matrix[a][b]
                if a == 0:
                    ans.append(dp[a][b])
                #ans.add(dp[a][b])
        
        for a in range(1,row):
            for b in range(0,col):
                dp[a][b] = dp[a-1][b]^dp[a][b]
                ans.append(dp[a][b])
                #ans.add(dp[a][b])
        ans.sort()
        return ans[-k]
    # 官方做法 二维前缀和加排序
    def kthLargestValue_office(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        results = list()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                results.append(pre[i][j])

        results.sort(reverse=True)
        return results[k - 1]
