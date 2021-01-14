from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 0:
            return ""
        head = strs[0]
        if length == 1:
            return head
        tail = 0
        for index,ch in enumerate(head):
            for s in strs:
                if s[index] != ch:
                    return head[0:tail]
            tail += 1
    # very interesting
    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        if not strs:
                return ''
        # 字典排序
        strs.sort()
        start = strs[0]
        end = strs[-1]
        for i,_ in enumerate(start):
            if start[i] == end[i]:
                continue
            else:
                return start[:i]
        return start
s = Solution()
print(s.longestCommonPrefix_2(["123"]))
