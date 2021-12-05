// 剑指 Offer 48. 最长不含重复字符的子字符串
// https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer48.cpp
@Time : 2021/12/05 21:34:30
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
     int left = 0, right = 0;
     vector<int> m(128,0);
     int maxlen = 0;
     while(right <s.length())
     {
         if(m[s[right]] > 0)
         {
             m[s[left]]--;
             left++;
             
         }
         else
         {
             m[s[right]]++;
             right++;
            if(maxlen < right-left)maxlen = right-left;
         }
     }
     return maxlen;
    }
};
