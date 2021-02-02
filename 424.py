from typing import List
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        left , right = 0,0
        freq = [0 for _ in range(26)]
        nmax = 0
        res = 0
        while right < l :
            freq[ord(s[right])-ord("A")] += 1
            nmax = max(nmax,freq[ord(s[right])-ord("A")])
            right +=1
            if right-left>nmax+k :
                freq[ord(s[left])-ord("A")]-=1
                left += 1
            res = max(res,right-left)
        return res
s = Solution()
print(s.characterReplacement("ABAB",2))

