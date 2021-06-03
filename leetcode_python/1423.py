from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = sum(cardPoints[0:k])
        max_value = curr
        left , right = 0,k-1
        while right >= 0:
            left -= 1
            curr = curr-cardPoints[right]+cardPoints[left]
            right -= 1
            if curr > max_value:
                max_value = curr
        return max_value
s = Solution()
print(s.maxScore([96,90,41,82,39,74,64,50,30],8))