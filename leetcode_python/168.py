# 168. Excel表列名称
# https://leetcode-cn.com/problems/excel-sheet-column-title/
# 26进制的转换问题
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            a0 = (columnNumber-1) %26 + 1
            ans.append(chr(a0 - 1 + ord("A")))
            columnNumber = (columnNumber - a0) // 26
        return "".join(ans[::-1])