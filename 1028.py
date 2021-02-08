class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right = 0 ,0
        l = len(s)
        curr = 0
        while right < l:
            curr += abs(ord(s[right])-ord(t[right]))
            right += 1
            if curr >  maxCost:
                curr -=abs(ord(s[left])-ord(t[left]))
                left +=1
        return l-left
s = Solution()
print(s.equalSubstring("abcd","cdef",1))