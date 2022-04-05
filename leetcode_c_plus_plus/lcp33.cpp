// 1566. 重复至少 K 次且长度为 M 的模式
// https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
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
@File : lcp33.cpp
@Time : 2022/03/30 22:25:45
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/class Solution {
public:
    bool containsPattern(vector<int>& arr, int m, int k) {
            int n = arr.size();
            for(int l = 0; l <= n - m * k; l++) {
                int offset;
                for(offset = 0; offset < m * k; offset++) {
                    if(arr[l + offset] != arr[l + offset % m]) {
                        break;
                    }
                }
                if (offset == m * k) {
                    return true;
                }
            }
            return false;
    }
};
