# 1658. 将 x 减到 0 的最小操作数
# https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_val = sum(nums)
        minus_val = total_val-x
        if minus_val < 0:
            return -1
        res = -1
        l = len(nums)
        left = 0
        right = 0
        sum_num = 0
        while right<l:
            sum_num += nums[right]
            while sum_num > minus_val:
                sum_num -= nums[left]
                left += 1
            if sum_num == minus_val:
                res = max(res,right-left+1)
            right += 1
            
        if res != -1:
            return l-res
        return -1
s = Solution()
print(s.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309],134365))