// 剑指 Offer 67. 把字符串转换成整数
// https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
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
@File : offer67.cpp
@Time : 2021/12/21 10:44:41
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int strToInt(string str) {
        if(str.empty()) return 0;
        if(str[0] >= 'a' && str[0] <= 'z') return 0;
        int i = 0;
        int max = pow(2, 31) - 1, min = -pow(2, 31);
        long res = 0;
        // 空格
        while(str[i] == ' ')
            i++;
        int sign = 1;
        // 负号
        if(str[i] == '-'){
            sign = -1;
            i++;
        }
        // 正号
        else if(str[i] == '+')
            i++;
        // 正式循环
        while(i < str.size()){
            if(str[i] >= '0' && str[i] <= '9'){
                res = res * 10 + sign * (str[i] - '0'); //核心：string to int
                // 超过范围就停止循环
                if(res > max)
                    return max;
                else if(res < min)
                    return min;
            }else{
                return res; // 只要遇到不是数字就停止循环
            }
            i++;
        }
        return res;
    }
};