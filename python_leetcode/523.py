# 523. 连续的子数组和
# https://leetcode-cn.com/problems/continuous-subarray-sum/
from typing import List
class Solution:
    # 暴力法  O(n^2)
    def checkSubarraySum_violent_way(self, nums: List[int], k: int) -> bool:
        # 构建前缀和
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        # 
        for a in range(1,len(prefix)):
            for b in range(a+1,len(prefix)):
                if (prefix[b]-prefix[a-1])%k == 0:
                    return True
        return False 
    # 使用了hash表 哈希的依据是同余
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        # 使用hash
        d = {0:-1}
        reminder = 0
        for index , val in enumerate(nums):
            reminder = (reminder+val)%k
            if reminder in d:
                if (index-d[reminder])>=2:
                    return True
            else:
                d[reminder] = index
        return False