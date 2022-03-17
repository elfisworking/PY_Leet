// 917. 仅仅反转字母
// https://leetcode-cn.com/problems/reverse-only-letters/
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
@File : 917.cpp
@Time : 2022/02/23 23:21:53
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    string reverseOnlyLetters(string s) {
        int left = 0, right = s.size() - 1;
        while(left < right) {
            while(left < right && !isalpha(s[left])) left++;
            while(left < right && !isalpha(s[right])) right--;
            if(left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;

    }
};