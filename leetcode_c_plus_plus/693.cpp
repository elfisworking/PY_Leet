// 693. 交替位二进制数
// https://leetcode-cn.com/problems/binary-number-with-alternating-bits/
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
@File : 693.cpp
@Time : 2022/03/28 10:01:38
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int prev = n & 1;
        n = (n >> 1);
        int curr = 0;
        while(n) {
            curr = n & 1;
            if(curr != prev) {
                prev = curr;
                n = (n >> 1);
            } else {
                return false;
            }
        }
        return true;
    }
};