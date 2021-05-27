# 1190. 反转每对括号间的子串
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    # 使用递归的方式
    def reverseParentheses_recursive(self, s: str) -> str:
        if not s:
            return ""
        l = len(s)
        h = 0
        def reverse(i):
            res = []
            while i<l:
                if s[i] == "(":
                    b , a =  reverse(i+1)
                    res += b
                    i = a
                elif s[i] == ")":
                    return res[::-1],i
                else:
                    res.append(s[i])
                i += 1
            return res
        res = reverse(0) 
        return "".join(res)

        # this use stack
    def reverseParentheses_stack(self, s: str) -> str:
        my_stack = []
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                my_stack.append(res)
                res = ""
            elif s[i] == ")":
                if my_stack:
                    res = my_stack.pop() + res[::-1]
            else:
                res += s[i]
        return res
    

s = Solution()
print(s.reverseParentheses_stack("(u(love)i)"))