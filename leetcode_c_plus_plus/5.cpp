// 5. 最长回文子串
// https://leetcode-cn.com/problems/longest-palindromic-substring/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
/**
@File : 5.cpp
@Time : 2021/11/09 15:05:56
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()) return "";
        int length = s.size();
        int left = 0, right = 0;
        int len = 1;
        int maxLen = 0;
        int start = 0;
        for(int i = 0; i < length; i++) {
            left = i - 1;
            right = i + 1;
            while(left >=0 && s[left] == s[i]) { left--; len++;}
            while(right < length && s[right] == s[i]) { right++; len++;}
            while(left >=0 && right < length && s[left] == s[right]) {
                len += 2;
                left--;
                right++;
            }
            if(len > maxLen) { maxLen = len; start = left;}
            len = 1;
        }
        return s.substr(start + 1, maxLen);
    }
};
class Solution_DP {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n < 2) return s;
        int maxLen = 1;
        int begin = 0;
        vector<vector<int>> dp(n, vector<int>(n));
        for (int i = 0; i < n; i++) dp[i][i] = true;
        for (int L = 2; L <= n; L++) {
            for (int i = 0; i < n ; i++) {
                int j = L + i - 1;
                if (j >= n) break;
                if (s[i] != s[j]) {
                    dp[i][j] = false;
                } else {
                    if (j - i < 3) {
                        dp[i][j] = true;
                    }else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                }
                if (dp[i][j] && j - i + 1 > maxLen) {
                maxLen = j - i + 1;
                begin = i;
                }
            }
        }
        return s.substr(begin, maxLen);
    }
};
