from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = dict()
        for d1, d2 in dominoes:
            # 排序后加入字典
            index = tuple(sorted((d1, d2)))
            if index in d:
                d[index] += 1
            else:
                d[index] = 1
        # 计算答案
        for i in d:
            ans += d[i] * (d[i] - 1) // 2
        return ans
    # 不使用hash表的方法  0~9 两两组合只有100种情况  拿这十种情况代替hash表即可 用
    def numEquivDominoPairs_1(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret

s = Solution()
print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))