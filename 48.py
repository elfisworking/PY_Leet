from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for a in range(m):
            for b in range(a+1,n):
                matrix[a][b] , matrix[b][a] = matrix[b][a],matrix[a][b]
        for a in matrix:
            a.reverse()
s = Solution()
print(s.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))
