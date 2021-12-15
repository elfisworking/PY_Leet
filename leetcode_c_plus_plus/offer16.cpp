//
//
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
@File : offer16.cpp
@Time : 2021/12/15 14:24:06
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    double myPow(double x, int n) {
        double res = 1;
        long long b = n;
        if(b < 0) {
            x = 1 / x;
            b = -b;
        }
        while(b) {
            if(b & 1) res *= x;
            x *= x;
            b >>= 1;
        }
        return res;
    }
};