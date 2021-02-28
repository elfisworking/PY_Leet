from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        l = len(A[0])-1
        for line  in A:
            temp = []
            for i in range(l,-1,-1):
                temp.append(line[i]^1)
            ans.append(temp)
        return ans
s = Solution()
print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))