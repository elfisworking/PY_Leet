// 剑指 Offer 14- II. 剪绳子 II
// https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
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
@File : offer14-II.cpp
@Time : 2021/12/27 21:54:16
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/
// 推论二： 尽可能将绳子以长度 33 等分为多段时，乘积最大。
class Solution {
public:
    int cuttingRope(int n) {
        if(n <= 3) return n - 1;
        int a = n / 3, c = n % 3;
        if(c == 1) {
            a = a -1;
            c = 4;
        }else if(c == 0) {
            c = 1;
        }
        long long ans = 1;
        long long x = 3;
        while(a > 0) {
            if(a & 1) ans = ( ans * x) % 1000000007;
            x = (x * x) % 1000000007;
            a >>= 1;
        }
        cout << ans << endl;
        ans = (ans * c) % 1000000007;
        return int(ans);

    }

};