from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = len(arr)
        if l < 2:
            return l
        left,right = 0 ,0
        ans_1 = 0
        while right < l-1:
            if right%2 == 0:
                if arr[right] < arr[right+1]:
                    right += 1
                else:
                    right += 1
                    ans_1 = max(ans_1,right-left)
                    left = right
            else:
                if arr[right]>arr[right+1]:
                    right += 1
                else:
                    right += 1
                    ans_1 = max(ans_1,right-left)
                    left = right
        ans_1 = max(ans_1,right-left+1)
        right , left = 0, 0
        ans_2 = 0
        while right < l-1:
            if right%2 == 0:
                if arr[right] > arr[right+1]:
                    right += 1
                else:
                    right += 1
                    ans_2 = max(ans_2,right-left)
                    left = right
            else:
                if arr[right]<arr[right+1]:
                    right += 1
                else:
                    right += 1
                    ans_2 = max(ans_2,right-left)
                    left = right
        ans = max(ans_1,ans_2,right-left+1)
        return ans
s  = Solution()
print(s.maxTurbulenceSize([0,8,45,88,48,68,28,55,17,24]))

           
