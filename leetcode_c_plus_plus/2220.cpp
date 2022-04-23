// 2220. 转换数字的最少位翻转次数
// https://leetcode-cn.com/problems/minimum-bit-flips-to-convert-number/
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
@File : 2220.cpp
@Time : 2022/04/19 22:20:39
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int minBitFlips(int start, int goal) {
        int a = start ^ goal;
        int ans = 0;
        while(a) {
            if(a & 1) ans++;
            a >>= 1;
        }
        return ans;
    }
};