from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        for a in range(col):
            temp = []
            for b in range(row):
                temp.append(matrix[b][a])
            ans.append(temp)
        return ans
s = Solution()
print(s.transpose([[1,2,3],[4,5,6]])) 