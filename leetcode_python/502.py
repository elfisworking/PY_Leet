from collections import defaultdict
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        d = defaultdict(list)
        for i in range(len(profits)):
            d[capital[i]].append(profits[i])
        cap = list(d.keys())
        current_profits = w
        for _ in range(k):
            if len(cap) == 0:
                return current_profits
            left , right = 0 ,len(cap)
            while left < right:
                mid = left + (right - left)//2
                if cap[mid] > current_profits:
                    right = mid
                else:
                    left = mid + 1
            pro = d[cap[left-1]]
            max_pro = max(pro)
            current_profits += max_pro
            pro.remove(max_pro)
            if len(pro) == 0:
                cap.pop(left-1)
        return current_profits

s = Solution()
print(s.findMaximizedCapital(10,0,[1,2,3],[0,1,2]))