from typing import List
class Solution:
    # 采用动态规划的方式解决
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [i for i in nums]
        l = len(nums)
        if l == 1:
            return nums[0]
        temp = 0
        for i in range(1,l):
            if dp[i] < dp[i]+dp[i-1]:
                dp[i] = dp[i]+dp[i-1]
            temp = max(temp,dp[i])
        return temp
    # 对动态规划的方式进行了优化
    def maxSubArray_1(self, nums: List[int]) -> int:
        ans, addup = nums[0], 0
        for num in nums:
            if addup > 0:
                addup += num
            else:
                addup = num
            ans = max(ans, addup)
        return ans
    # 分治的思想 划分为两段 左left 和 right  分别得出left的最大值和right的最大值
    # 跟跨越left right两端的最大值进行比较 相对于dp更加的写法上更加的复杂 时间复杂
    # 度相同 但是有着更大的空间复杂度
s =  Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))