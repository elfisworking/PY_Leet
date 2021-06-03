from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        begin = 0
        while begin < l:
            if nums[begin] == target:
                break
            else:
                begin +=1
        end = begin
        while end < l:
            if nums[end] == target:
                end += 1
            else:
                break 
        if begin == l:
            return [-1,-1]
        return [begin,end-1]
    # 使用二分查找找的一个target 然后再从这个target进行中心扩散
    def searchRange_binarySearch(self,nums:List[int],target:int)-> List[int]:
        l = len(nums)
        left ,right  = 0,l-1
        m = -1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                m = middle # 这是中心 
                break 
            if nums[middle] > target:
                right = middle-1
            else:
                left = middle + 1
        # 然后中心扩散
        if m == -1:
            return [-1,-1]
        left , right = m,m
        while True:
            if left >= 0 and nums[left] == target:
                left -= 1
            elif right < l and nums[right] == target:
                right += 1
            else:
                break
        return [left+1,right-1]
                
        
s = Solution()
print(s.searchRange_binarySearch([1,1,1,2,2,3,3,6],1))