// 剑指 Offer 15. 二进制中1的个数
// https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
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
@File : offer15.cpp
@Time : 2021/12/16 14:19:53
@Author : YuMin Zhang
@State : Indepeedent
@Thinking : bit operation
@Tag : Easy
**/
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        for(int i = 0; i < 32; i ++) {
            if(n & 1) ans++;
            n >>= 1;
        }
        return ans;
    }
};

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        while (n) {
            n &= n - 1;
            ret++;
        }
        return ret;
    }
};

/*
位优化 n & (n - 1)
*/