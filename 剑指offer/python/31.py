# 剑指 Offer 31. 栈的压入、弹出序列
# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack  = []
        index = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        
        if stack:
            return False
        return True

s = Solution()
print(s.validateStackSequences([1,2,3,4,5],[4,3,5,1,2]))