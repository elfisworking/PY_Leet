// 954. 二倍数对数组
// https://leetcode-cn.com/problems/array-of-doubled-pairs/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
#include<iostream>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 954.cpp
@Time : 2022/04/01 10:19:18
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        unordered_map<int, int> map;
        sort(arr.begin(), arr.end());
        for(int i = 0; i < arr.size(); i++) {
            if( arr[i] > 0) {
                if(arr[i] % 2  == 0 && map[arr[i] / 2] > 0) {
                    cout << arr[i] / 2 << " " << arr[i] << "--" << endl;
                    map[arr[i] / 2]--;
                } else {
                    cout << arr[i ] <<"++" << endl;
                    map[arr[i]]++;
                }
            } else if(arr[i] < 0) {
                if(map[arr[i] * 2] > 0) {
                    map[arr[i] * 2]--;
                } else{
                    map[arr[i]]++;
                }
            }
        }
        for(auto& x : map) {
            cout << x.first << " " << x.second << endl;
            if(x.second > 0) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    vector<int> arr{4, -2, 2, -4};
    s.canReorderDoubled(arr);
    return 0;
}