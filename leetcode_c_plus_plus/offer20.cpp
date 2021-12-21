//
//
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
@File : offer20.cpp
@Time : 2021/12/21 10:56:46
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking : fuck
@Tag :  Medium
**/
class Solution {
public:
    bool isNumber(string s) {
        int n = s.size();
        int index = -1;
        bool hasDot = false,hasE = false,hasOp = false,hasNum = false;
        while(index<n && s[++index]==' ');
        while(index<n){
            if('0'<=s[index] && s[index]<='9'){
                hasNum = true;
            }else if(s[index]=='e' || s[index]=='E'){
                if(hasE || !hasNum) return false;
                hasE = true;
                hasOp = false;hasDot = false;hasNum = false;
            }else if(s[index]=='+' || s[index]=='-'){
                if(hasOp || hasNum || hasDot) return false;
                hasOp = true;
            }else if(s[index]=='.'){
                if(hasDot || hasE) return false;
                hasDot = true;
            }else if(s[index]==' '){
                break;
            }else{
                return false;
            }
            ++index;
        }
        while(index<n && s[++index]==' ');
        return hasNum && index==n;
    }
};