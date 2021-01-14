from typing import List
class Solution:
    # firt iter
    def prefixesDivBy5_1(self, A: List[int]) -> List[bool]:
        ans = []
        res = 0
        for i in A:
            res = res * 2 + i
            if res%5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
    # second iter faster
     def prefixesDivBy5_2(self, A: List[int]) -> List[bool]:
        ans = []
        res = 0
        for i in A:
            res = ((res<<1) + i)%5
            ans.append(not res)
        return ans
    # third iter  fastest
    def prefixesDivBy5_3(self, A: List[int]) -> List[bool]:
        ans = []
        res = 0
        for i in A:
            res = (res * 2 + i)%5
            if res ==  0:
                ans.append(True)
            else:
                ans.append(False)
            # ans.append(res)
        return ans
s = Solution()
print(s.prefixesDivBy5_1([0,1,1,1,1,1]))
