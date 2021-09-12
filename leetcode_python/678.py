# 678. 有效的括号字符串
# https://leetcode-cn.com/problems/valid-parenthesis-string/
from collections import Counter
class Solution:
    #def checkValidString(self, s: str) -> bool:
        # if not str:
        #     return True       
        # counter =  Counter(s)
        # asterisk = None
        # if counter["("] > counter[")"]:
        #     asterisk = ")"
        # elif counter["("] < counter[")"]:
        #     asterisk = "(" 
        # stack = []
        # for i in s:
        #     if i == "(":
        #         stack.append(i)
        #     elif i == "*":
        #         if asterisk:
        #             stack.append(asterisk)
        #     else:
        #         if stack:
        #             stack.pop()
        #         else:
        #             return False
        # if not stack:
        #     return True
        # return False
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        asterisk_stack = []
        for index, i in enumerate(s):
            if i == "(":
                left_stack.append(index)
            elif i == "*":
                asterisk_stack.append(index)
            else:
                if left_stack:
                    left_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False
        while left_stack and asterisk_stack:
            left_index = left_stack.pop()
            asterisk_index = asterisk_stack.pop()
            if left_index > asterisk_index:
                return False
        if not left_stack:
            return True
        return False