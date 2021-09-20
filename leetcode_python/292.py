# 292. Nim 游戏
# https://leetcode-cn.com/problems/nim-game/
# 找规律的题 需要多列举几个
# 独立完成
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return False
        return True