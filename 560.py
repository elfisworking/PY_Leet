# 560. 和为K的子数组
# https://leetcode-cn.com/problems/subarray-sum-equals-k/
from typing import List
from collections import defaultdict

class Solution:
    # 用双指针的方法 有局限性 无法使用
    def subarraySum_two_pointer(self, nums: List[int], k: int) -> int:
        left = right = 0
        sum = 0
        res = 0
        while right < len(nums):
            sum += nums[right]
            while left <= right and sum > k :
                sum -= nums[left]
                left += 1
            while left<= right and sum == k:
                res += 1
                sum -= nums[left]
                left += 1
            right += 1
        return res
    # 直接使用前缀和 时间超时无法AC
    def subarraySum_prefix(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        res = 0
        for a in range(len(nums)):
            for b in range(a,len(nums)):
                tmp = prefix[b+1]-prefix[a]
                if tmp == k:
                    res += 1
        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0 
        d = defaultdict(int)
        # 这里要注意{0：1} 这个表示 k = prefix 即
        d[0] = 1
        res = 0
        for i in nums:
            prefix += i
            if prefix - k in d:
                res += d[prefix-k]
            d[prefix] += 1
        return res

s = Solution()
print(s.subarraySum_prefix([0,0,0],0))