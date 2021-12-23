// 剑指 Offer 59 - II. 队列的最大值
// https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/

#include <bits/stdc++.h>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer59.cpp
@Time : 2021/12/22 17:07:13
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
**/
class MaxQueue {
    queue<int> q;
    deque<int> d;
public:
    MaxQueue() {
    }
    
    int max_value() {
        if (d.empty())
            return -1;
        return d.front();
    }
    
    void push_back(int value) {
        while (!d.empty() && d.back() < value) {
            d.pop_back();
        }
        d.push_back(value);
        q.push(value);
    }
    
    int pop_front() {
        if (q.empty())
            return -1;
        int ans = q.front();
        if (ans == d.front()) {
            d.pop_front();
        }
        q.pop();
        return ans;
    }
};
