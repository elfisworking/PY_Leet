class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = list()
        l  = len(S)
        ans.append(S[0])
        for i in range(1,l):
            if len(ans)!= 0 and ans[-1] == S[i]:
                ans.pop()
            else:
                ans.append(S[i])
        return "".join(ans)
s = Solution()
print(s.removeDuplicates("abbbacaa"))