// 925. 长按键入
// https://leetcode-cn.com/problems/long-pressed-name/
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
@File : 925.cpp
@Time : 2022/03/29 21:01:38
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int idx = 0;
        int name_length = name.size(), typed_name = typed.size();
        if(typed_name < name_length) return false;
        char prev = name[0];
        for(int i = 0; i < name_length; i++) {
            while(idx < typed_name && typed[idx] != name[i]) {
                if(prev != typed[idx]) return false;
                prev = typed[idx];
                idx++;
            }
            prev = typed[idx];
            idx++;
            if(idx > typed_name) return false;
        }
        while(idx < typed_name && typed[idx - 1] == typed[idx]) {
            idx++;
        }
        return idx == typed_name ? true : false;
    }   
};

class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int j = 0;
        int i = 0;
        while(j < typed.size()) {
            if(i < name.size() and name[i] == typed[j]) {
                i++;
                j++;
            } else if(j > 0 and typed[j - 1] == typed[j]) j++;
            else return false;
        }
        return i == name.size();
    }
};