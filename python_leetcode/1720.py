# 1720. 解码异或后的数组
# https://leetcode-cn.com/problems/decode-xored-array/
from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for en in encoded:
            first = first ^ en
            print(first)
            res.append(first)
        return res
s = Solution()