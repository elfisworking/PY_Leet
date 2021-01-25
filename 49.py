from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for val in strs:
            t = list(val)
            t.sort()
            t = "".join(t)
            if t not in h:
                h[t]=[val]
            else:
                temp = h[t]
                temp.append(val)
                h[t] = temp
        return list(h.values())
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
