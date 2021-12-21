// 89. 格雷编码
// https://leetcode-cn.com/problems/gray-code/
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
@File : 89.cpp
@Time : 2021/12/21 19:48:48
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res{0};
        int head = 1;
        for(int i = 0; i < n; i++) {
            for(int j = res.size() - 1; j >=0; j--) {
                res.push_back(res[j] + head);
            }
            head <<= 1;
        }
        return res;

    }
};