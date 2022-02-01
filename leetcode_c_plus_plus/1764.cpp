// 1763. 最长的美好子字符串
// https://leetcode-cn.com/problems/longest-nice-substring/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 1764.cpp
@Time : 2022/02/01 21:17:51
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    string longestNiceSubstring(string s) {
        int l = s.size();
        int maxPos = 0;
        int maxLen = 0;
        for(int i = 0; i < l; i++) {
            int lower = 0;
            int upper = 0;
            for(int j = i; j < l; j++) {
                if('a' <= s[j] && s[j] <= 'z') {
                    lower |= 1 << (s[j] - 'a');
                } else {
                    upper |= 1 << (s[j] - 'A');
                }
                if(lower == upper && j - i + 1 > maxLen){
                    maxLen = j - i + 1;
                    maxPos = i;
                }
            }
        }
        return s.substr(maxPos, maxLen); 

    }
};