# 1456. 定长子串中元音的最大数目
# https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    # 典型的滑动窗口题目
    def maxVowels(self, s: str, k: int) -> int:
        counter = 0
        char = ["a","e","i","o","u"]
        for i in range(k):
            if s[i] in char:
                counter += 1
        max_value = counter
        left , right = 0 , k
        while right < len(s):
            if s[right] in char:
                counter += 1
            if  s[left] in char:
                counter -= 1
            max_value = max(max_value,counter)
            right += 1
            left += 1
        return max_value

