// 6. Z 字形变换
// https://leetcode-cn.com/problems/zigzag-conversion/
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
@File : 6.cpp
@Time : 2022/03/01 16:41:48
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        int mod = (numRows - 2) * 2 + 2;
        string ans;
        for(int i = 0; i < numRows; i++) {
            for(int j = 0; j < s.size(); j++) {
                if(i == 0) {
                    if(j % mod == 0)
                        ans.push_back(s[j]); 
                } else if(i == numRows - 1) {
                    if(j % mod == numRows - 1)
                        ans.push_back(s[j]);
                } else{
                    if(j % mod == i || j % mod == (mod - i)  ) {
                        ans.push_back(s[j]);

                    }
                }
            }
        }
        return ans;
    }
};