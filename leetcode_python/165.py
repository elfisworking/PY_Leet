# 165. 比较版本号
# https://leetcode-cn.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1 = len(v1)
        l2 = len(v2)
        l = max(l1,l2)
        for i in range(l):
            if i < l1:
                n1 = int(v1[i])
            else:
                n1 = 0
            if i < l2:
                n2 = int(v2[i])
            else:
                n2 = 0
                
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0

s = Solution()
print(s.compareVersion("1.02.001","1.002"))