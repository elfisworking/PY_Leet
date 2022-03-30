//
//
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
@File : 680.cpp
@Time : 2022/03/29 21:21:55
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool validPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while(left < right) {
            if(s[left] == s[right]) {
                left++;
                right--;
            } else {
                break;
            }
        }
        if(left >= right) return true;
        int l1 = left + 1;
        int r1 = right - 1;
        while(l1 < right) {
            if(s[l1] == s[right]) {
                l1++;
                right--;
            } else {
                break;
            }
        }
        if(l1 >= right) return true;
        while(left < r1) {
            if(s[left] == s[r1]) {
                left++;
                r1--;
            } else {
                break;
            }
        }
        return left >= r1 ? true : false;
    }
};