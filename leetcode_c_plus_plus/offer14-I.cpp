// 剑指 Offer 14- I. 剪绳子
// https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
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
@File : 14-I.cpp
@Time : 2021/12/19 13:21:17
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
**/
// error
// class Solution {
// public:
//     int cuttingRope(int n) {
//         int a = sqrt(n);
//         int b = a + 1;
//         int num1 = mul(a, n);
//         int num2 = mul(b, n);
//         return num1 > num2 ? num1 : num2;

//     }

//     int mul(int a, int n) {
//         if( a == 1) return 0;
//         int c = n / a;
//         return pow(c, a - 1) * (n - c * (a - 1));

//     }

// };

class Solution {
public:
int cuttingRope(int n) {
    return n <= 3? n - 1 : pow(3, n / 3) * 4 / (4 - n % 3);
}
};