# 1239. 串联字符串的最大长度
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
from typing import List
# DFS 位计算  剪枝
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def check(s):
            return len(set(s)) == len(s)
        
        def backtrack(path, selected):
            nonlocal res
            if len(path) > res and check(path):
                res = len(path)
            for i in range(len(selected)):
                backtrack(path+selected[i], selected[i+1:])
        
        res = 0
        backtrack("", arr)
        return res
    
    def maxLength_offical(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if ((mask >> idx) & 1):   # // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx   # 将 ch 加入 mask 中
            if mask > 0:
                masks.append(mask)

        ans = 0

        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count("1"))
                return
            
            if (mask & masks[pos]) == 0:   # mask 和 masks[pos] 无公共元素
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)
        
        backtrack(0, 0)
        return ans