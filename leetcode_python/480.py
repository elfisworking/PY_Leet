from typing import List
class Solution:
    # 暴力方法  耗时 5124ms
    def medianSlidingWindow_violent_function(self, nums: List[int], k: int) -> List[float]:
        l = len(nums)
        left ,right = 0,k-1
        mid = right//2
        flag = False
        if k%2 == 0:
            flag = True
        ans = []
        while right<l:
            temp = nums[left:right+1]
            temp.sort()
            if flag:
                ans.append((temp[mid+1]+temp[mid])/2)
            else:
                ans.append(temp[mid])
            right += 1
            left += 1
        return ans
    # 
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

                


