// 806. 写字符串需要的行数
// https://leetcode-cn.com/problems/number-of-lines-to-write-string/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<string>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 806.cpp
@Time : 2022/03/25 15:42:17
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1;
        int curr_length = 0;
        for(int i = 0; i < s.size(); i++) {
            curr_length += widths[s[i] - 'a'];
            if(curr_length > 100) {
                lines++;
                curr_length = widths[s[i] - 'a'];
            }
        }
        return vector<int>{lines, curr_length};
    }
};