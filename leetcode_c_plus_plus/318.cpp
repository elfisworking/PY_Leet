// 318. 最大单词长度乘积
// https://leetcode-cn.com/problems/maximum-product-of-word-lengths/
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
@File : 318.cpp
@Time : 2022/03/28 09:47:43
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> bits;
        for(auto& str : words) {
            int tmp = 0;
            for(int i = 0; i < str.size(); i++) {
                tmp |= (1 << (str[i] - 'a'));
            }
            bits.emplace_back(tmp);
        }
        int ans = 0;
        for(int i = 0; i < bits.size(); i++) {
            for(int j = i + 1; j < bits.size(); j++) {
                if((bits[i] & bits[j]) == 0) {
                    ans = max(ans, int(words[i].size() * words[j].size()));
                }
            }
        }
        return ans;
    }
};