// 剑指 Offer 65. 不用加减乘除做加法
// https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
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
@File : offer65.cpp
@Time : 2021/12/16 14:25:05
@Author : YuMin Zhang
@State : Depedent
@Tag : Easy
**/

// bad
// class Solution {
// public:
//     int add(int a, int b) {
//         if(a == 0) return b;
//         if(b == 0) return a;
//         int c = a ^ b;
//         int carry = 0;
//         int pt = 1;
//         for(int i = 1; i < 31; i++) {
//             c ^= carry;
//             carry = c & carry;
//             carry <<= i; 
//         }
//         return c;
//     }
// };

class Solution {
public:
    int add(int a, int b) {
        while (b) {
            int carry = a & b; // 计算 进位
            a = a ^ b; // 计算 本位
            b = (unsigned)carry << 1;
        }
        return a;
    }
};