# 457 环形数组是否存在循环
# https://leetcode-cn.com/problems/circular-array-loop/comments/
from typing import List
class Solution:
    # this method 38/41 cases passed
    # can not handle this case [3,1,2]
    # then add 12~17 line ,still failure
    # can't pass case [1,-1,2,4,4]
    def circularArrayLoop_failure(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 2 :
            return False
        start = 0
        for i in range(l):
            if i != (i+nums[i])%l:
                start = i 
                break
        slow = fast= ptr =  start
        while True:
            slow = (slow + nums[slow])%l
            fast = (fast + nums[fast])%l
            fast = (fast + nums[fast])%l
            if fast == slow:
                while ptr != slow:
                    ptr =(ptr +  nums[ptr])%l
                    slow = (slow + nums[slow])%l
                break

        next = (ptr + nums[ptr])%l
        if next == ptr:
            return False
        if nums[ptr] > 0:
            while next != ptr:
                if nums[next] < 0:
                    return False
                next = (next + nums[next])%l
            return True
        else:
            while next != ptr:
                if nums[next] > 0:
                    return False
                next = (next  + nums[next])%l
            return True

    # solution:判断每一个点是否存在环里面，在的话打上标记。然后从没打上标记的开始，继续探索
    # 环，直到所有的点都扫描过了。这时，如果不存在符合要求的环 返回False ,有则返回True
    def circularArrayLoop(self, nums: List[int]) -> bool:
            
        numLength = len(nums)
        indexToNext = {index: (index + value) % numLength for index, value in enumerate(nums)}
        increment = {key: value for key, value in indexToNext.items() if key != value}
          
        while len(increment) > 0:
            
            if any(index == nextIndex for index, nextIndex in increment.items()):
                return True
            
            increment = {index: indexToNext[nextIndex] 
                         for index, nextIndex in increment.items() 
                         if nums[index] * nums[nextIndex] > 0 and nextIndex in increment}            
            
        return False
s = Solution()
print(s.circularArrayLoop([1,1,2]))