# 1074. 元素和为目标值的子矩阵数量
# https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target/
from typing import List
from collections import defaultdict
class Solution:
    # 抄的答案 不会做 需要复习 
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n , m = len(matrix) , len(matrix[0])
        sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                sum[i][j] = sum[i-1][j] + sum[i][j-1]-sum[i-1][j-1]+matrix[i-1][j-1]
        
        ans = 0
        for top in range(1,n+1):
            for bot in range(top,n+1):
                cur = 0
                d = defaultdict(int)
                for r in range(1,m+1):
                    cur = sum[bot][r]-sum[top-1][r]
                    if cur == target:
                        ans += 1
                    if (cur - target) in d:
                        ans += d[cur-target]
                    d[cur] += 1
        return ans
                    

        