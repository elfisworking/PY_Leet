# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left , right = 0, 0
        res = 0
        char = set()
        while right < len(s):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            res = max(res,right-left+1)
            right += 1
        return res
s = Solution()
print(s.lengthOfLongestSubstring("aaa"))