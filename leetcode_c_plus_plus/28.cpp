// 28. 实现 strStr()
// https://leetcode-cn.com/problems/implement-strstr/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
#include<iostream>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 28.cpp
@Time : 2022/01/04 20:11:50
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
**/
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size() == 0) return 0;
        int n = haystack.size();
        int m = needle.size();
        haystack = " " + haystack;
        needle = " " + needle;
        vector<int> next_list(m + 1, 0);
        int j = 0;
        for(int i = 2; i < m; i++) {
            while(j > 0 && needle[i] != needle[j + 1]) { j = next_list[j]; }
            if(needle[i] == needle[j + 1]) { 
                j++;
            }
            next_list[i] = j;
        }
        cout << m << endl;
        j = 0;
        for(int i = 1; i < n + 1; i++) {
            while(j > 0 && haystack[i] != needle[j + 1]) j = next_list[j];
            if(haystack[i] == needle[j + 1]) j++;
            if(j == m) return i - m;
        }
        return -1;


    }
};
int main() {
    Solution s;
    int index = s.strStr("aabaaabaaac", "aabaaac");
    cout << index << endl;
    return 0;
}
