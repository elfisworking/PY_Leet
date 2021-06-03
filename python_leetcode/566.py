from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]):
            return nums
        ans = []
        num = 0
        row = []
        for line in nums:
            for v in line:
                num += 1
                if num%c == 0:
                    row.append(v)
                    ans.append(row)
                    row  = []
                else:
                    row.append(v)
        return ans 
s = Solution()
print(s.matrixReshape([[1,2,3],[4,5,6]],3,2))