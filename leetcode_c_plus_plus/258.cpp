// https://leetcode-cn.com/problems/add-digits/
// 258. 各位相加
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
@File : 258.cpp
@Time : 2022/03/03 22:08:02
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int addDigits(int n) {
        while(n >= 10) {
            int tmp = 0;
            while(n > 0) {
                tmp += n % 10;
                n = n / 10;
            }
            n = tmp;
        }
        return n;
    }
};