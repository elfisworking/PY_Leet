from typing import List
class Solution:
    # 暴力算法 超时
    # def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    #     ans = []
    #     sum_a = sum(A)
    #     sum_b = sum(B)
    #     for i in A:
    #         for b in B:
    #             if sum_a-i+b==sum_b-b+i:
    #                 ans.append(i)
    #                 ans.append(b)
    #                 return ans
    #
    # 采用了集合的方式
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        # 这里处理需要注意
        y = (sum_a-sum_b)//2
        rec = set(A)
        ans = None
        for b in B:
            a = y+b
            if a in rec:
                ans = [a,b]
                break
        return ans
s =Solution()
print(s.fairCandySwap([2],[1,3]))