# 剑指 Offer II 006. 排序数组中两个数字之和
# https://leetcode-cn.com/problems/kLl5u1/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0 , len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left,right]