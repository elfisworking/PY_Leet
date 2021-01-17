from typing import List
class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     def back(n):
    #         if n == 1:
    #             return {"()"}
    #         else:
    #             res =set()
    #             for i in back(n-1):
    #                 res.add("()"+i)
    #                 res.add("("+i+")")
    #                 res.add(i+"()")
    #             return res
    #     res = back(n)
    #     return list(res).sort()
    def generateParenthesis_1(self, n: int) -> List[str]:
        ans = []
        def backtrack(S,left,right):
            if len(S) == 2 * n:
                ans.append("".join(S))
            if left < n:
                S.append("(")
                backtrack(S,left+1,right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S,left,right+1)
                S.pop()
        backtrack([],0,0)
        return ans
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s,left,right):
            if len(s) == 2 *n :
                ans.append(s)
                return
            if left < n:
                backtrack(s+"(",left+1,right)
            if right < left:
                backtrack(s+")",left,right+1)
        backtrack("",0,0)
        return ans
    
            


s = Solution()
print(s.generateParenthesis(3))
                    
            
        