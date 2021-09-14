from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        h = [0] * len(words)
        for i in range(len(words)):
            a = 0
            for ch in words[i]:
                a |= (1<<ord(ch)-ord("a"))
            h[i] = a
        
        max_len = 0
        for a in range(len(words)):
            l = len(words[a])
            for b in range(a+1,len(words)):
                if h[a] & h[b] == 0:
                    max_len = max(max_len, l * len(words[b]))
        return max_len

s = Solution()
print(s.maxProduct())