// 剑指 Offer 31. 栈的压入、弹出序列
// https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<stack>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer31.cpp
@Time : 2021/12/20 20:03:15
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int l = pushed.size();    
        if(l == 0) return true;  

        int j = 0;
        stack<int> s;
        for(int i = 0; i < l; i++){
            while(!s.empty() && s.top() == popped[j]) {
                j++;
                s.pop();
            }
            s.push(pushed[i]);

        }

        while(j < l && !s.empty() && s.top() == popped[j]) {
            j++;
            s.pop();
        }
        return s.empty();

    }
};