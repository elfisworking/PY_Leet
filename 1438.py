from typing import List 
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        s  = SortedList()
        l = len(nums)
        left , right = 0 , 0
        while right < l:
            s.add(nums[right])
            if s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            right += 1
        return right - left
    # offical method 
    def longestSubarray_2(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        queMax, queMin = deque(), deque()
        left = right = ret = 0

        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()
            
            queMax.append(nums[right])
            queMin.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1
            
            ret = max(ret, right - left + 1)
            right += 1
        
        return ret


