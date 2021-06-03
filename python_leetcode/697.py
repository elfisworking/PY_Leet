from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()
        for i, v in enumerate(nums):
            if v in mp:
                mp[v][0] +=1
                mp[v][2] = i
            else:
                mp[v] = [1,i,i]
        maxNum = minLen = 0
        for count , left , right in mp.values():
            if maxNum < count:
                maxNum = count 
                minLen =  right - left + 1
            elif maxNum == count:
                if minLen > (span := right - left + 1) :
                    minLen = span
        return minLen


        