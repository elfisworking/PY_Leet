// 537. 复数乘法
// https://leetcode-cn.com/problems/complex-number-multiplication/
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
@File : 537.cpp
@Time : 2022/02/25 23:45:37
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        int idx1 = getIndex(num1);
        int idx2 = getIndex(num2);
        int real_num1 = getNum(num1, 0, idx1);
        int vir_num1 = getNum(num1, idx1 + 1, num1.size() - 1);
        int real_num2 = getNum(num2, 0, idx2);
        int vir_num2 = getNum(num2, idx2 + 1, num2.size() - 1);
        int real_num = real_num1 * real_num2 - vir_num1 * vir_num2;
        int vir_num = real_num1 * vir_num2 + real_num2 * vir_num1;
        return to_string(real_num) + "+" + to_string(vir_num) + "i";

    }
    
    int getIndex(string & str) {
        for(int i = 0; i < str.size(); i++) {
            if(str[i] == '+') return i;
        }
        return -1;
    }
    
    int getNum(string & str, int begin, int end) {
        string tmp = "";
        for(int i = begin; i < end; i++) {
            tmp.push_back(str[i]);
        }
        return stoi(tmp);
    }
};