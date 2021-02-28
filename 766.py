from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for a in range(m-1):
            for b in range(n-1):
                if matrix[a][b] != matrix[a+1][b+1]:
                    return False
        return True
s =Solution()
print(s.isToeplitzMatrix([[1,2],[2,2]]))