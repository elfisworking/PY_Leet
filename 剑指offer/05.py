# 剑指 Offer 05. 替换空格
# https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")