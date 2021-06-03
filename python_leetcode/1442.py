# 1442. 形成两个异或相等数组的三元组数目
# https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        l = len(arr)
        # 使用三重循环 可以通过前缀和来减少时间复杂度
        # 但是除了这种方法 还有其它方法吗 来减少时间复杂度
        count = 0
        for a in range(0,l-1):
            sum = 0
            for b in range(a,l):
                sum ^= arr[b]
                if sum == 0 and b > a :
                    count += b -a
        return count