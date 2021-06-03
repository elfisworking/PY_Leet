from typing import List
# class NumMatrix:
#     # 通过一维进行二维的拼接 一维的计算方式看leetcode 303题
#     def __init__(self, matrix: List[List[int]]):
#         row = len(matrix)
#         col = len(matrix[0])
#         d = [[0] for _ in range(row)]
#         for a in range(row):
#             for b in range(col):
#                 d[a].append(d[a][-1]+matrix[a][b])
#         self.d = d


#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         res = 0
#         for a in range(row1,row2+1):
#             res += self.d[a][col2+1]-self.d[a][col1]
#         return res
class NumMatrix:
    # 直接进行二维的计算
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            row , col  = 0,0
        else:
            row ,col = len(matrix),len(matrix[0])
        self.preSum = [[0]*(col+1) for _ in range(row+1)]
        for  a in range(row):
            for b in range(col):
                self.preSum[a+1][b+1]=self.preSum[a][b+1]+self.preSum[a+1][b]-self.preSum[a][b]+matrix[a][b]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1]-self.preSum[row2+1][col1]-self.preSum[row1][col2+1]+self.preSum[row1][col1]
s = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
print(s.sumRegion(1,1,2,2))