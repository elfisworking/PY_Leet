// 941. 有效的山脉数组
// https://leetcode-cn.com/problems/valid-mountain-array/
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
@File : 941.cpp
@Time : 2022/04/02 22:09:26
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int left = 1;
        int l = arr.size();
        if(l <= 2) return false;
        int right = l - 2;
        while(left < l ){
            if(arr[left - 1] >= arr[left]) break;
            left++;
        }
        while(right >= 0 ) {
            if(arr[right] <= arr[right + 1]) break;
            right--;
        }
        return right + 2 == left && left != l && right != -1;
    }
};