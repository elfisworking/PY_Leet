from typing import List
class Solution:
    # 超时
    # def chalkReplacer(self, chalk: List[int], k: int) -> int:
    #     i = 0
    #     l = len(chalk)
    #     while True:
    #         i = i%l
    #         if k >= chalk[i]:
    #             k -= chalk[i]
    #         else:
    #             break
    #         i += 1
    #     return i
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k = k % s 
        tmp = 0
        for i in range(len(chalk)):
            tmp += chalk[i]
            if tmp > k:
                return i