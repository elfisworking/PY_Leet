from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for en in encoded:
            fisrt = first ^ en
            print(first)
            res.append(first)
        return res
s = Solution()