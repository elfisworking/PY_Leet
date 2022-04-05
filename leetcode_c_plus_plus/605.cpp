// 605. 种花问题
// https://leetcode-cn.com/problems/can-place-flowers/
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
@File : 605.cpp
@Time : 2022/03/31 22:41:43
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int size = flowerbed.size();
        for(int i = 0; i < size; i++) {
            if(flowerbed[i] == 0) {
                if(i > 0 && i < size - 1 && flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0 ) {
                    flowerbed[i] = 1;
                    n--;
                } else if(i == 0) {
                    if(i < size - 1 && flowerbed[i + 1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                    if(i == size - 1) {
                        n--;
                    }
                } else if(i == size - 1) {
                    if(i > 0 && flowerbed[i - 1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
            }
        }
        return n <= 0;
    }
};