from typing import List
class Solution:
    # error
    def maxArea_error(self, height: List[int]) -> int:
        max_index = height.index(max(height))
        max_value=  0
        for i in range(0,len(height)):
            value = height[i]*abs(max_index-i)
            if value > max_value:
                max_value = value
        return max_value
    # method : double pointer
    def maxArea(self, height: List[int]) -> int:
        start , end = 0,len(height)-1
        res , temp = 0,0
        while start < end:
            if height[start] < height[end]:
                temp = height[start] * (end-start)
                start += 1
            else:
                temp = height[end]*(end-start)
                end -= 1
            if temp > res:
                res = temp
        return res
            
s = Solution()
print(s.maxArea([1,2,1]))